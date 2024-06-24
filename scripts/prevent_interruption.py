import gradio as gr
from modules import script_callbacks, shared, ui_extensions

preventInterruption: bool = False

def warn():
    text = "Interruptions are blocked"
    print(f'\n{text}\n', flush=True)
    gr.Warning(text)

def hijackOne(oldFunction):
    def newFunction(*args, **kwargs):
        if preventInterruption:
            warn()
            return None
        else:
            return oldFunction(*args, **kwargs)
    return newFunction


def hijack():
    shared.state.interrupt = hijackOne(shared.state.interrupt)
    if hasattr(shared.state, 'stop_generating'):
        shared.state.stop_generating = hijackOne(shared.state.stop_generating)
    shared.state.skip = hijackOne(shared.state.skip)

    ui_extensions.apply_and_restart = hijackOne(ui_extensions.apply_and_restart)
    shared.state.request_restart = hijackOne(shared.state.request_restart)


hijack()


def setPreventInterruption(value: bool):
    global preventInterruption
    preventInterruption = value


def beforeFooter(component, **kwargs):
    if kwargs.get('elem_id', None) != 'footer':
        return
    with gr.Blocks(elem_id='prevent_interruption_block') as block:
        prevent_interruption = gr.Checkbox(False, label='',
            elem_id='prevent_interruption_checkbox',
            elem_classes=['prevent_interruption_checkbox']
        )
        gr.HTML('<label id="prevent_interruption_label" '
                       'for="prevent_interruption_input" '
                       'class="prevent_interruption_label"'
                '>Prevent interruption</label>')
        fetchPreventInterruption = gr.Button(visible=False, elem_id='prevent_interruption_fetch_button')
    prevent_interruption.change(fn=setPreventInterruption, inputs=[prevent_interruption], outputs=[], show_progress=False)
    fetchPreventInterruption.click(fn=lambda: preventInterruption, inputs=[], outputs=[prevent_interruption], show_progress=False)

script_callbacks.on_before_component(beforeFooter)

