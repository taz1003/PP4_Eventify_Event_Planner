document.addEventListener("DOMContentLoaded", function () {
    const deleteEventButtons = document.querySelectorAll('.delete-event');
    const deleteEventForm = document.getElementById('deleteEventForm');

    deleteEventButtons.forEach((button) => {
        button.addEventListener('click', () => {
            const eventSlug = button.getAttribute('data-event_slug');
            deleteEventForm.action = `/${eventSlug}/delete/`;
        });
    });
});
