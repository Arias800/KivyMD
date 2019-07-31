import re
from distutils.core import setup

setup(
    name="kivymd",
    version=version,
    description="Set of widgets for Kivy inspired by Google's Material " "Design",
    author="Andrés Rodríguez, author fork - HeaTTheatR",
    author_email="andres.rodriguez@lithersoft.com, email author fork "
    "- kivydevelopment@gmail.com",
    url="https://github.com/HeaTTheatR/KivyMD",
    packages=["kivymd"],
    package_data={
        "kivymd": [
            "images/*.png",
            "images/*.jpg",
            "images/*.atlas",
            "fonts/*.ttf",
            "vendor/*.py",
            "vendor/circleLayout/*.py",
            "vendor/circularTimePicker/*.py",
            "vendor/navigationdrawer/*.py",
            "toast/*.py",
            "toast/kivytoast/*.py",
            "toast/androidtoast/*.py",
            "stiffscroll/*.py",
            "utils/*.py",
        ]
    },
    requires=["kivy", "pillow"],
)
