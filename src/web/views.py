from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

from . import tasks


@cache_control(no_cache=True, must_revalidate=True, no_store=True, max_age=0)
def index(request):
    return render(request, "index.html", {})


@csrf_exempt
def compute(request):
    def _format_rouge_result(rouge):
        return "P: {:.1f} | R: {:.1f} | F1: {:.1f}".format(
            rouge["precision"], rouge["recall"], rouge["f1"]
        )

    if request.method == "POST":
        references = tasks.parse_string(request.POST.get("references", ""))
        predictions = tasks.parse_string(request.POST.get("predictions", ""))

        result = {}
        if request.POST.get("checkbox_sentence_bleu", False) == "true":
            result["sentence_bleu"] = "{:.1f}".format(
                tasks.sentence_bleu(references, predictions)
            )
        if request.POST.get("checkbox_corpus_bleu", False) == "true":
            result["corpus_bleu"] = "{:.1f}".format(
                tasks.corpus_bleu(references, predictions)
            )
        if request.POST.get("checkbox_rouge1", False) == "true":
            result["rouge1"] = _format_rouge_result(
                tasks.rouge("1", references, predictions)
            )
        if request.POST.get("checkbox_rouge2", False) == "true":
            result["rouge2"] = _format_rouge_result(
                tasks.rouge("2", references, predictions)
            )
        if request.POST.get("checkbox_rougeL", False) == "true":
            result["rougeL"] = _format_rouge_result(
                tasks.rouge("L", references, predictions)
            )
        if request.POST.get("checkbox_tf1", False) == "true":
            result["tf1"] = "{:.1f}".format(tasks.tf1(references, predictions))

        return JsonResponse(result)

    return JsonResponse({"error": "Invalid request method"})
