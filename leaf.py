def leafac(x,y,leaf,b,n,cright,cleft):
    X=x
    if bullet==True:
        for i in range(10):
            pygame.time.delay(-1)
            win.blit(leaf,(X,y))
            X+=10
            if X>=900:
                X=x
                break
            print(X)
            if (left==True) and (right==False):
                win.blit(cleft[b],(x,y))
                b+=1
            if (right==True)and (left==False):
                win.blit(cright[n],(x,y))
                n+=1
            if (b==4) or (n==4):
                b=0
                n=0
            pygame.display.update()
            win.blit(bg,(0,0))
            if X>=900:
                X=x
                break
            print(X)
                
            pygame.display.update()
            win.blit(bg,(0,0))
