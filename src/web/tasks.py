import ast
import statistics

import sacrebleu
from rouge_score import rouge_scorer


def sentence_bleu(references, predictions):
    scores = []
    for reference, prediction in zip(references, predictions):
        scores.append(
            sacrebleu.sentence_bleu(
                prediction,
                reference if isinstance(reference, list) else [reference],
                smooth_method="exp",
                smooth_value=0.0,
                lowercase=True,
                tokenize="intl",
            ).score
        )

    return statistics.mean(scores)


def corpus_bleu(references, predictions):
    return sacrebleu.corpus_bleu(
        predictions,
        references,
        smooth_method="exp",
        smooth_value=0.0,
        lowercase=True,
        tokenize="intl",
    ).score


def rouge(scope, references, predictions):
    rouge = f"rouge{scope}"
    scorer = rouge_scorer.RougeScorer([rouge], use_stemmer=True)
    references = [r if isinstance(r,list) else [r] for r in references]

    scores_dict = {"precision": 0, "recall": 0, "f1": 0}

    for refs, prediction in zip(references, predictions):
        best_f1 = 0
        for ref in refs:
            scores = scorer.score(ref, prediction)
            if scores[rouge].fmeasure > best_f1:
                best_f1 = scores[rouge].fmeasure
                scores_dict["precision"] += scores[rouge].precision
                scores_dict["recall"] += scores[rouge].recall
                scores_dict["f1"] += scores[rouge].fmeasure

    return {k: v / len(references) for k, v in scores_dict.items()}


def parse_string(string):
    try:
        return list(ast.literal_eval(string))
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing string: {e}")
        return None
