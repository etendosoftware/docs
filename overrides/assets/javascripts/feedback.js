function updateFeedbackLink(elementId, formId) {
    const feedbackLink = document.getElementById(elementId);
    if (feedbackLink) {
        const currentPath = window.location.pathname;
        const formUrl = `https://docs.google.com/forms/d/${formId}/viewform?entry.1159911930=${encodeURIComponent(currentPath)}`;
        feedbackLink.href = formUrl;
    }
}

function updateNegativeFeedbackLink() {
    updateFeedbackLink("n-feedback-link", "15xgzQaUTdaxS6Z_jM0h4zYP4ebALOWmDz__pG2JLFb0");
}

function updatePositiveFeedbackLink() {
    updateFeedbackLink("p-feedback-link", "1agexla60x2li2t5OZf9CV2Jd7P_B9Ecc1d2VK7lUNLw");
}

document.addEventListener("DOMContentLoaded", updateNegativeFeedbackLink);
document.addEventListener("DOMContentLoaded", updatePositiveFeedbackLink);

const observer = new MutationObserver(() => {
updateNegativeFeedbackLink();
updatePositiveFeedbackLink();
});

observer.observe(document.body, { childList: true, subtree: true });
window.addEventListener("popstate", updateNegativeFeedbackLink);
window.addEventListener("popstate", updatePositiveFeedbackLink);
