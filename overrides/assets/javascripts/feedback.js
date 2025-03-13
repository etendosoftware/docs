function updateFeedbackLink() {
    const feedbackLink = document.getElementById("feedback-link");
    if (feedbackLink) {
    const currentPath = window.location.pathname;
    const formUrl = `https://docs.google.com/forms/d/15xgzQaUTdaxS6Z_jM0h4zYP4ebALOWmDz__pG2JLFb0/viewform?entry.1159911930=${encodeURIComponent(currentPath)}`;
    feedbackLink.href = formUrl;
    }
}

document.addEventListener("DOMContentLoaded", updateFeedbackLink);

const observer = new MutationObserver(() => {
updateFeedbackLink();
});

observer.observe(document.body, { childList: true, subtree: true });
window.addEventListener("popstate", updateFeedbackLink);
