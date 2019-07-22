import pygame

class PlayerLogic:

    def __init__(self):
        #add Start Brick to prev Bricks
        startBrick = Brick(0,0,0,90)
        startBrick.field_id = "C8"
        self.prev_Bricks = [startBrick]

    def setPrev_Bricks(self,brick):
        if(len(self.prev_Bricks) >= 2):
            self.prev_Bricks.pop(0)
        self.prev_Bricks.append(x)

    def completeCheck(self,brick):
        return tileIsConnected(brick)



    def isEndReached(self,brick):
        if(brick.field_id == "O10"):
            return True
        else:
            return False


    def tileIsConnected(self,brick):

        prevprev_Brick_fieldId = prev_Bricks[0].field_id
        prevprev_id_letter = prevprev_Brick_fieldId[0]
        prevprev_id_number = prevprev_Brick_fieldId[1:]

        prev_Brick_fieldId = prev_Bricks[1].field_id
        prev_id_letter = prev_Brick_fieldId[0]
        prev_id_number = prev_Brick_fieldId[1:]

        field_id = brick.field_id

        #previous Brick is straight
        if(prev_Bricks[1].type == 0):
            if(prev_Bricks[1].rotation >= 80 and prev_Bricks[1].rotation <= 90 or prev_Bricks[1].rotation <= -80 and prev_Bricks[1].rotation >= -90):
                if("".join(chr(ord(prevprev_id_letter)+1)+prevprev_id_number) == prev_Bricks[1].field_id): # If Bahn kommt von links
                    if("".join(chr(ord(prev_id_letter)+1)+prev_id_number) == field_id):
                        return True
                else:
                    if("".join(chr(ord(prev_id_letter)-1)+prev_id_number) == field_id):
                        return True

            elif(prev_Bricks[1].rotation >= -10 and prev_Bricks[1].rotation <= 10 or prev_Bricks[1].rotation <= -170 and prev_Bricks[1].rotation >= -180):
                if("".join(prevprev_id_letter+str(int(prevprev_id_number)+1)) == prev_Bricks[1].field_id): # If Bahn kommt von oben
                    if("".join(prev_id_letter+str(int(prevprev_id_number)+1)) == field_id):
                        return True
                else: # If Bahn kommt von Unten
                    if("".join(prev_id_letter+str(int(prevprev_id_number)-1)) == field_id):
                        return True

        #previous Brick is curved
        elif(prev_Bricks[1].type == 1):


            if(prev_Bricks[1].rotation >= 80 and prev_Bricks[1].rotation <= 90):
                if("".join(chr(ord(prevprev_id_letter)+1)+prevprev_id_number) == prev_Bricks[1].field_id): # If Bahn kommt von Links
                    if("".join(prev_id_letter+str(int(prev_id_number)-1)) == field_id):
                        return True
                else: # If Bahn kommt von oben
                    if("".join(chr(ord(prev_id_letter)-1)+prev_id_number) == field_id):
                        return True

            if(prev_Bricks[1].rotation >= -10 and prev_Bricks[1].rotation <= 10):
                if("".join(prevprev_id_letter+str(int(prevprev_id_number)+1)) == prev_Brick_fieldId): #If Bahn kommt von Oben
                    if("".join(chr(ord(prev_id_letter)-1)+prev_id_number) == field_id):
                        return True
                else: #If Bahn kommt von rechts
                    if("".join(prevprev_id_letter+str(int(prevprev_id_number)-1)) == field_id):
                        return True

            if(prev_Bricks[1].rotation >= -190 and prev_Bricks[1].rotation <= -170):
                if("".join(chr(ord(prevprev_id_letter)+1)+prevprev_id_number) == prev_Bricks[1].field_id): # If Bahn kommt von links
                    if("".join(prev_id_letter+str(int(prevprev_id_number)+1)) == field_id):
                        return True
                else: # If Bahn kommt von unten
                    if("".join(chr(ord(prev_id_letter)-1)+prev_id_number) == field_id):
                        return True

            if(prev_Bricks[1].rotation >= -100 and prev_Bricks[1].rotation <= -80):
                if("".join(prevprev_id_letter+str(int(prevprev_id_number)-1)) == prev_Bricks[1].field_id): # If Bahn kommt von unten
                    if("".join(chr(ord(prev_id_letter)-1)+prev_id_number) == field_id):
                        return True
                else: # if Bahn kommt von rechts
                    if("".join(prev_id_letter+str(int(prev_id_number)+1)) == field_id):
                        return True





    def placeTile(self,fieldId):
        # execute python script on niryo
        pass
