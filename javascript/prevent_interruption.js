var prevent_interruption_registered = false;

onUiUpdate(function () {
    if (prevent_interruption_registered) return;
    let input = gradioApp().querySelector('.prevent_interruption_checkbox input');
    let label = gradioApp().getElementById('prevent_interruption_label');
    let footer = gradioApp().getElementById('footer');
    if (!input || !label || !footer) return;

    input.id = 'prevent_interruption_input';
    input.addEventListener('change', function() {
        // Toggle a class on the label based on the input's checked state
        if (this.checked) {
            label.classList.add('checked');
        } else {
            label.classList.remove('checked');
        }
    });

    footer.appendChild(label);

    prevent_interruption_registered = true;
    console.log('!!! registered');
});
