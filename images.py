"""Images manipulations."""

import os
from typing_extensions import Annotated
from PIL import Image, ImageOps
import typer

app = typer.Typer()

@app.command()
def convert_webp(
    directory: Annotated[str, typer.Argument(help='Directory of pictures to convert')],
    img_format: Annotated[str, typer.Argument(help='Format to convert pictures into')] = 'jpeg',
    delete: Annotated[bool, typer.Option(help='Delete original pictures when converted')] = True):
    """Convert a WEBP image into another format."""

    paths = []
    for entry in os.scandir(directory):
        if entry.path.endswith('webp'):
            paths.append(entry.path)

    count = 1
    for path in paths:
        new_name = path.split('.webp')[0]
        img = Image.open(path).convert('RGB')
        img.save(f'{new_name}.{img_format}', img_format)
        print(f'{count}/{len(paths)} done')
        count += 1

        if delete:
            os.remove(path)


@app.command()
def thumbnail(
    image: Annotated[str, typer.Argument(help='Image to create a thumbnail of')],
    width: Annotated[str, typer.Argument(help='Width of the thumbnail')],
    height: Annotated[str, typer.Argument(help='Height of the thumbnail')],
    output: Annotated[str, typer.Argument(help='Name of the thumbnail')]
):
    """Create a thumbnail of a picture."""

    image = Image.open(image)
    fixed_image = ImageOps.exif_transpose(image)
    fixed_image.thumbnail((int(width), int(height)))
    fixed_image.save(output)


if __name__ == '__main__':
    app()
