python early:
    import singleton
    if not config.developer:
        me = singleton.SingleInstance()

#启动页
label splashscreen:
    image cubelogo:
        "stickers/cubelogo.png"
        zoom 1
        align(0.5,0.5)

    if not config.developer:
        $ renpy.movie_cutscene("audio/video/开场动画.webm")

    return


# 周目相关持久化变量
default persistent.be1 = False
default persistent.be2 = False
default persistent.be3 = False
default persistent.ne = False
default persistent.ge = False
default persistent.te = False
default persistent.playthrough = 1  # 周目数

define persistent.lightRead = False
define persistent.showCP = True


init python:
    def check_playthrough():
        # 一周目中完成所有be和ne后，才能进二周目
        if(persistent.playthrough == 1 and
           persistent.be1 and
           persistent.be2 and
           persistent.be3 and
           persistent.ne):
               persistent.playthrough = 2
        # 二周目中完成ge后进入三周目
        if(persistent.playthrough == 2 and persistent.ge):
            persistent.playthrough = 3
        if persistent.te:
            persistent.playthrough = 4

        renpy.save_persistent()
        renpy.log((persistent.be1, persistent.be2, persistent.be3, persistent.ne, persistent.ge, persistent.te))
        renpy.log("周目数: %s" % persistent.playthrough)
    import os
    def check_develop():
        config.developer = os.path.exists(os.path.expanduser('~') + '\.zhijiang\develop.txt')
        config.rollback_enabled = config.developer
    check_develop()

#游戏在此开始。

label start:
    $ check_playthrough()
    jump cp0_start
