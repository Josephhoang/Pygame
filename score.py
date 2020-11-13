def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Cars Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,red)
    gamedisplays.blit(text,(5,50))
    gamedisplays.blit(score,(5,30))
