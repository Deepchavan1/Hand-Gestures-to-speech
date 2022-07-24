import HandTrackingModule as htm
import os
import time
import mediapipe as mp
import cv2
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages/')


def get():
    wCam, hCam = 640, 480

    cap = cv2.VideoCapture(0)

    cap.set(3, wCam)
    cap.set(4, hCam)

    

    pTime = 0

    detector = htm.handDetector(detectionCon=0.75)

    tipIds = [4, 8, 12, 16, 20]

    flag = True
    num = 0
    row_num = 0
    col_num = 0
    isZ = False
    isSpace = False
    isEnd = False

    while num != 2:
        time.sleep(0.3)
        success, img = cap.read()
        img = detector.findHands(img)

        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0 and num != 2:
            # for thumb
            if lmList[8][2] > lmList[7][2] and lmList[12][2] > lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] > lmList[3][1]:
                print("thumb")
                isZ = True
                break
                break

            # index finger
            if lmList[8][2] < lmList[7][2] and lmList[12][2] > lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] < lmList[3][1]:
                print("index")
                print("inc numb")
                if num == 0:
                    print("row index")
                    row_num = 1
                    num = num + 1
                    time.sleep(0.5)
                else:
                    print("col index")
                    col_num = 1
                    time.sleep(0.5)
                    num = num + 1

                # if num == 2:
                #     break

            # index and middle finger
            elif lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] < lmList[3][1]:
                print("index+middle")
                if num == 0:
                    print("row index")
                    row_num = 2
                    time.sleep(0.5)
                    num = num + 1
                else:
                    print("col index")
                    col_num = 2
                    time.sleep(0.5)
                    num = num + 1

                # if num == 2:
                #     break

            # index and middle and ring finger
            elif lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] < lmList[3][1]:
                print("index+middle+ring")
                if num == 0:
                    print("row index")
                    row_num = 3
                    time.sleep(0.5)
                    num = num + 1
                else:
                    print("col index")
                    col_num = 3
                    time.sleep(0.5)
                    num = num + 1

                # if num == 2:
                #     break

            # index and middle and ring and little finger
            elif lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2] and lmList[4][1] < lmList[3][1]:
                print("index+middle+ring+little")
                if num == 0:
                    print("row index")
                    row_num = 4
                    time.sleep(0.5)
                    num = num + 1
                else:
                    print("col index")
                    col_num = 4
                    time.sleep(0.5)
                    num = num + 1

                # if num == 2:
                #     break

            # index and middle and ring and little finger and thumb
            elif lmList[8][2] < lmList[7][2] and lmList[12][2] < lmList[11][2] and lmList[16][2] < lmList[15][2] and lmList[20][2] < lmList[19][2] and lmList[4][1] > lmList[3][1]:
                print("index+middle+ring+little+thumb")
                if num == 0:
                    print("row index")
                    row_num = 5
                    time.sleep(0.5)
                    num = num + 1
                else:
                    print("col index")
                    col_num = 5
                    time.sleep(0.5)
                    num = num + 1

                # if num == 2:
                #     break

            # little finger
            elif lmList[8][2] > lmList[7][2] and lmList[12][2] > lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] < lmList[19][2] and lmList[4][1] < lmList[3][1]:
                isEnd = True
                time.sleep(0.5)
                num = 2
                # if num == 2:
                #     break

            # index and thumb finger
            elif lmList[8][2] < lmList[7][2] and lmList[12][2] > lmList[11][2] and lmList[16][2] > lmList[15][2] and lmList[20][2] > lmList[19][2] and lmList[4][1] > lmList[3][1]:
                isSpace = True
                time.sleep(0.5)
                num = 2
                # if num == 2:
                #     break

            else:
                cv2.putText(img, str('not identified'), (45, 375),
                            cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        # if isZ:
        #     print("isZ")
        # else:
        #     print("not isZ")
        print(row_num, col_num)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.imshow("Image", img)
        cv2.waitKey(3)
    
    return row_num, col_num, isZ, isSpace, isEnd


if __name__=="__main__":
    letters = (['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], [
        'k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'])

    z = 'z'

    cont = True

    toSpeak = ''

    while(cont):
        row_num, col_num, isZ, isSpace, isEnd = get()
        if(row_num != 0 and col_num != 0):
            print(letters[row_num-1][col_num-1])
            toSpeak += letters[row_num-1][col_num-1]
        
        elif(isZ):
            print('z')
            toSpeak += 'z'
        
        elif(isSpace):
            print('space')
            toSpeak += ' '
        
        elif(isEnd):
            print('end')
            cont = False

    print(toSpeak)
    os.system("say " + toSpeak)


    


    
