label te_cp9_start:
    $ goTe = True 
    jump cp9_g_start.part1

label cp9_g_start:
    $ goTe = False 

    jump cp9_g_start.part1


label .part1:
    window hide
    $ save.cp_name = "第九章"
    $ goNe = False

    if not config.developer:
        show screen unskip
        $ _skipping = False
    $ renpy.movie_cutscene("audio/video/start/9.webm")
    if not config.developer:
        hide screen unskip
        $ _skipping = True
    jump cp8_n.part2



label cp9_g_end:
    if goTe:
        jump geGoTe
    else:
        jump ge

