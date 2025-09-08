/* jshint esversion: 6 */
// JavaScript to handle dynamic form action for deleting comments
document.addEventListener("DOMContentLoaded", function () {
    // Handle delete buttons
    const deleteButtons = document.querySelectorAll('.delete-comment');
    const deleteConfirmLink = document.getElementById('deleteConfirm');

    deleteButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const commentId = button.getAttribute('data-comment_id');
            const slug = window.location.pathname.split('/')[1]; // Assumes URL format: /<slug>/
            deleteConfirmLink.href = `/${slug}/comment/delete/${commentId}`;
        });
    });
});
