#! /usr/bin/env python

# 自帶模組。
import sys
# 自帶模組。
import os
# 用於建立臨時資料夾。
import tempfile
# 日志系統。
import logging


class SingleInstanceException(BaseException):
    pass


class SingleInstance:

    # 基本介紹。
    """
    If you want to prevent your script from running in parallel just instantiate SingleInstance() class. If is there another instance already running it will throw a `SingleInstanceException`.

    >>> import tendo
    ... me = SingleInstance()

    This option is very useful if you have scripts executed by crontab at small amounts of time.

    Remember that this works by creating a lock file with a filename based on the full path to the script file.

    Providing a flavor_id will augment the filename with the provided flavor_id, allowing you to create multiple singleton instances from the same file. This is particularly useful if you want specific functions to have their own singleton instances.
    """

    def __init__(self, flavor_id=""):
        import sys
        # 判斷初始化。
        self.initialized = False
        # 基礎名稱。
        # os.path.splitext(path) 分離檔案名稱與拓展後綴。
        # os.path.abspath(path) 擷取絕對路徑。
        # sys.argv 從程式外部向内部遞送參數。
        # .replace(oldstr, newstr,*max) 將字符串的字符進行替換。
        basename = os.path.splitext(os.path.abspath(sys.argv[0]))[0].replace(
            "/", "-").replace(":", "").replace("\\", "-") + '-%s' % flavor_id + '.lock'
        # os.path.splitext(os.path.abspath(
        # sys.modules['__main__'].__file__))[0].replace(
        # "/", "-").replace(":", "").replace("\\", "-") + '-%s' % flavor_id + '.lock'
        #os.path.normpath 標準化位址，合并多餘分隔符和上級引用，格式化位址為"A/B"
        self.lockfile = os.path.normpath(
            #tempfile.gettempdir 用于返回保存临时文件的文件夹路径.
            tempfile.gettempdir() + '/' + basename)
        # Logger.debug 自定義函數，輸出Debug的Log訊息。
        logger.debug("SingleInstance lockfile: " + self.lockfile)
        # sys.platform 返回當前作業系統訊息。
        if sys.platform == 'win32':
            #Try。
            try:
                # file already exists, we try to remove (in case previous
                # execution was interrupted)
                # os.path.exists(path) 判斷資料夾或者檔案是否存在。
                if os.path.exists(self.lockfile):
                    # os.unlink(path) 刪除檔案，如果并非檔案則會返回錯誤。
                    os.unlink(self.lockfile)
                    # os.open(file,flags,*mode) 開啓一個檔案，並設定需要打開的選項。
                self.fd = os.open(
                    # os.O_CREAT 建立一個新檔。
                    # os.O_EXCL 如果指定的檔案已經存在，則返回錯誤。
                    # os.O_ROWR 以讀寫方式打開。
                    self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            except OSError:
                # sys.exc_info() 擷取異常的詳細訊息。
                type, e, tb = sys.exc_info()
                if e.errno == 13:
                    # 輸出error級別的Log
                    logger.error(
                        "Another instance is already running, quitting.")
                    raise SingleInstanceException()
                print(e.errno)
                raise
        else:  # non Windows
            # fcntl 為檔案加密。
            import fcntl
            # 以寫方式打開。
            self.fp = open(self.lockfile, 'w')
            self.fp.flush()
            try:
                # 為檔案加鎖。
                # fcntl.LOCK_EX 排他锁。
                # fcntl.LOCK_NB 非阻塞锁。
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                logger.warning(
                    "Another instance is already running, quitting.")
                raise SingleInstanceException()
        self.initialized = True

    def __del__(self):
        import sys
        import os
        if not self.initialized:
            return
        try:
            if sys.platform == 'win32':
                if hasattr(self, 'fd'):
                    # os.close(fd) 關閉檔案描述字元。
                    os.close(self.fd)
                    os.unlink(self.lockfile)
            else:
                import fcntl
                fcntl.lockf(self.fp, fcntl.LOCK_UN)
                # os.close(self.fp)
                # os.path.isfile(path) 判別path所指是否是一個普通檔案。
                if os.path.isfile(self.lockfile):
                    os.unlink(self.lockfile)
        except Exception as e:
            if logger:
                logger.warning(e)
            else:
                print("Unloggable error: %s" % e)
            # sys.exit(arg) 程式退出，arg為狀態判別。
            # 0為正常；非0為異常。
            sys.exit(-1)


def f(name):
    # level 指定Log輸出類別，輸出結果等級最小為級別。
    tmp = logger.level
    logger.setLevel(logging.CRITICAL)  # we do not want to see the warning
    try:
        me2 = SingleInstance(flavor_id=name)  # noqa
    except SingleInstanceException:
        sys.exit(-1)
    logger.setLevel(tmp)
    pass

# logging.getLogger(name) 擷取Logger實例，若name為空則返回root Logger
logger = logging.getLogger("tendo.singleton")
# logging.addHandler() 為Logger添加Logger處理器。
# logging.StreamHandler() 控制臺日志。
logger.addHandler(logging.StreamHandler())
