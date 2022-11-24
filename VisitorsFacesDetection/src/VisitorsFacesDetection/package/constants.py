WINDOW_TITLE = "Розпізнавання облич на відео"
WINDOW_BACKGROUND = "#f2dbff"
ICON = "ico/icon.ico"

BTN_FRAME_COLOR = 'lightgreen'


DISKS_CAPTIONS = "wmic logicaldisk get  DriveType, caption"

# Paths

#VIDEOS_FOLDER = "C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/dataset/videos"
VIDEOS_FOLDER = "dataset/videos"

#PHOTOS_FOLDER = "C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/dataset/photos"
PHOTOS_FOLDER = "dataset/photos"
FULL_PATH_TO_PHOTOS_FOLDER = "C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/src/VisitorsFacesDetection/dataset/photos"

#SNAPSHOTS_FOLDER = "C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/screenshots"

SNAPSHOTS = "snapshots"


PROCESSED_PHOTOS_FOLDER = "dataset/photos/processed photos"

SELECT_VIDEO = "Оберіть відеозапис"
SELECT_IMG = "Оберіть зображення"

LAUNCH = "Відеофайл обрано, можна починати розпізнавання"

VIDEOTYPES = (("MP4 files", "*.mp4"),
        ("WMV files", "*.wmv"),
        ("AVI files", "*.avi"))

IMGTYPES = (("JPEG", "*.jpg"),
         ("PNG", "*.png"),
         ("GIF", "*.gif"))

IMAGE_ENDS_WITH = ('jpg', 'png', 'gif')

FACE_RECOG_MODEL = "model/faces.xml"


PC_DISKS = ('C', 'D')

IMAGES_FOLDER_ON_USB_FLASH_DRIVE = 'photos'

# frame settings
MAX_FRAME_WIDTH = 860
MAX_FRAME_HEIGHT = 480

# button settings
BTN_W = 20 

# Messages and titles
TITLE_ERROR = "Виникла помилка!"
NOT_SELECTED = 'Відеофайл не відтворюється або не обраний!'
CANT_LAUNCH = "Неможливо відтворити відеофайл!"
#CANT_STOP = "Відео не запущено!"
CANT_ADD_IMAGES = "Спочатку вставте накопичувач з папкою \"photos\";"\
+ "\nТакож перевірте розташування цільвої директорії для колекції" 
CANT_DISPLAY_VIDEO = "Розмір відео завеликий!"
NO_VISITORS = "Визначених в колекції зображень користувачів на відео не зафіксовано!"


FAQ_STEP1 = "Оновіть колекцію зображень, вставивши накопичувач з колекцією в папці \"photos\""
FAQ_STEP2 = "Оберіть відеозапис для перегляду та дослідження"
FAQ_STEP3 = "Виконайте запуск, ставте відео на паузу, робіть скріншоти"
FAQ_STEP4 = "Здійснюйте розпізнавання; результати будуть надіслані повідомленням в Telegram"


# Labels on buttons
SELECT_VIDEO = "Вибрати відеозапис"
START_RECOGNITION = "Виконати розпізнавання"
NEW_IMAGES = "Додати нові фото"
FAQ = "Довідка"
PLAY = "Запуск відео"
PAUSE = "Пауза"
RELAUNCH = "Продовжити"
SNAPSHOT = "Знімок"

