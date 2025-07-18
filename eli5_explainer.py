import eli5
from eli5.sklearn import explain_prediction_sklearn
from sklearn.base import ClassifierMixin

def explain_with_eli5(model: ClassifierMixin, cleaned_text: str, vectorizer):
    explanation = eli5.format_as_html(
        explain_prediction_sklearn(model, cleaned_text, vec=vectorizer)
    )
    return explanation
