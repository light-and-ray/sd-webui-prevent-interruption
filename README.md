# Prevent Interruption

This is an extension for [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) which adds a switch in page footer to prevent user from accidental interrupting

![](images/img1.jpg)
![](images/img2.jpg)

If enabled, it blocks any `interrupt`, `stop_generating` and `skip` command no matter from where: buttons, api, or even from [sd-webui-cli-interruption](https://github.com/light-and-ray/sd-webui-cli-interruption). Also it blocks "Apply and restart" and "Reload Ui" buttons

Useful if you are processing a big batch or a video. Also I recomment you to install [close-confirmation-dialogue](https://github.com/w-e-w/sdwebui-close-confirmation-dialogue) extension
