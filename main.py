import sys

from pyqt5_plugins.examplebuttonplugin import QtGui

from movie_recommendations import movie_recommendations
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_default import Ui_DefaultWindow
from ui_image import Ui_Image
from ui_mainWindow import Ui_MainWindow
from ui_movies_window import Ui_Dialog
import take_a_picture_age_gender


class DefaultWindow(QMainWindow):
    """
    A class for the default window
    """

    def __init__(self):
        super(DefaultWindow, self).__init__()
        self.ui = Ui_DefaultWindow()
        self.dialog = None
        self.ui.setupUi(self)

    def on_pushButton_clicked(self):
        self.close()
        self.dialog = MainWindow()  # The next window
        self.dialog.show()


class MainWindow(QMainWindow):
    """
    A class for the main window
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.dialog = None
        self.ui.setupUi(self)

    def on_pushButton_clicked(self):
        age = None
        while not age:
            image = take_a_picture_age_gender.take_a_picture()
            age, gender, frame_face_path = take_a_picture_age_gender.get_data_from_face(image)
        self.close()
        self.dialog = ImageWindow(frame_face_path, age, gender)  # The next window
        self.dialog.show()


class ImageWindow(QMainWindow):
    """
    A class for the image window
    """

    def __init__(self, frame_face_path, age, gender):
        super(ImageWindow, self).__init__()
        self.ui = Ui_Image()
        self.image = frame_face_path
        self.dialog = None
        self.ui.setupUi(self)
        self.dnext(age, gender)

    def dnext(self, age, gender):
        movies_list = movie_recommendations(age, gender)
        self.close()
        self.dialog = MovieWindow(movies_list)  # The next window
        self.dialog.show()


class MovieWindow(QMainWindow):
    """
    A class for the movies window
    """

    def __init__(self, movies_list):
        super(MovieWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.dialog = None
        self.movies = movies_list
        self.ui.setupUi(self)

    def on_pushButton_clicked(self):
        self.close()
        self.dialog = DefaultWindow()  # The next window
        self.dialog.show()

    def get_movies(self):
        return self.movies


def apply_default_window():
    """
    A function that open the default window
    """
    app = QApplication(sys.argv)
    window = DefaultWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    apply_default_window()
