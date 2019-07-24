import PlayerLogic
import socket

class RobotLogic:

    def __init__(self):
        self.nextBrick = None
        self.next_fieldID = ""
        self.next_Rotation = 0
        self.prev_Bricks = []
        self.directionFromPrevToCurrentBrick = ""

    def updatePrevBricks(self,bricks):
        self.prev_Bricks = bricks
        return True

    def setNextTile(self,brick):
        self.nextBrick = brick
        return True

    def getNextFieldId(self):
        if(len(self.prev_Bricks)>=2):
            prevprev_Brick_fieldId = self.prev_Bricks[0].field_id
            prevprev_id_letter = prevprev_Brick_fieldId[0]
            prevprev_id_number = prevprev_Brick_fieldId[1:]

            prev_Brick_fieldId = self.prev_Bricks[1].field_id
            prev_id_letter = prev_Brick_fieldId[0]
            prev_id_number = prev_Brick_fieldId[1:]

            #previous Brick is straight
            print ("prevprev Index: ",prevprev_Brick_fieldId," Rotation: ",self.prev_Bricks[0].r_Rasterisiert ,"\nprev Index: ",prev_Brick_fieldId," Rotation: ",self.prev_Bricks[0].r_Rasterisiert)
            if(self.prev_Bricks[1].type == 0):
                if(self.prev_Bricks[1].rotation >= 80 and self.prev_Bricks[1].rotation <= 90 or self.prev_Bricks[1].rotation <= -80 and self.prev_Bricks[1].rotation >= -90):
                    if("".join(chr(ord(prevprev_id_letter)+1)+prevprev_id_number) == self.prev_Bricks[1].field_id): # If Bahn kommt von links
                        self.next_fieldID = "".join(chr(ord(prev_id_letter)+1)+prev_id_number)
                        self.directionFromPrevToCurrentBrick = "rechts"
                    else:
                        self.next_fieldID = "".join(chr(ord(prev_id_letter)-1)+prev_id_number)
                        self.directionFromPrevToCurrentBrick = "links"

                elif(self.prev_Bricks[1].rotation >= -10 and self.prev_Bricks[1].rotation <= 10 or self.prev_Bricks[1].rotation <= -170 and self.prev_Bricks[1].rotation >= -190):
                    if("".join(prevprev_id_letter+str(int(prevprev_id_number)+1)) == self.prev_Bricks[1].field_id): # If Bahn kommt von oben
                        self.next_fieldID = "".join(prev_id_letter+str(int(prevprev_id_number)+1))
                        self.directionFromPrevToCurrentBrick = "unten"
                    else: # If Bahn kommt von Unten
                        self.next_fieldID = "".join(prev_id_letter+str(int(prevprev_id_number)-1))
                        self.directionFromPrevToCurrentBrick = "oben"

            #previous Brick is curved
            elif(self.prev_Bricks[1].type == 1):
                if(self.prev_Bricks[1].rotation >= 80 and self.prev_Bricks[1].rotation <= 90):
                    if("".join(chr(ord(prevprev_id_letter)+1)+prevprev_id_number) == self.prev_Bricks[1].field_id): # If Bahn kommt von Links
                        self.field_id = "".join(prev_id_letter+str(int(prev_id_number)-1))
                        self.directionFromPrevToCurrentBrick = "oben"
                    else: # If Bahn kommt von oben
                        self.field_id = "".join(chr(ord(prev_id_letter)-1)+prev_id_number)
                        self.directionFromPrevToCurrentBrick = "links"

                if(self.prev_Bricks[1].rotation >= -10 and self.prev_Bricks[1].rotation <= 10):
                    if("".join(prevprev_id_letter+str(int(prevprev_id_number)+1)) == prev_Brick_fieldId): #If Bahn kommt von Oben
                        self.field_id = "".join(chr(ord(prev_id_letter)-1)+prev_id_number)
                        self.directionFromPrevToCurrentBrick = "links"
                    else: #If Bahn kommt von rechts
                        self.field_id = "".join(prevprev_id_letter+str(int(prevprev_id_number)-1))
                        self.directionFromPrevToCurrentBrick = "oben"

                if(self.prev_Bricks[1].rotation >= -190 and self.prev_Bricks[1].rotation <= -170):
                    if("".join(chr(ord(prevprev_id_letter)+1)+prevprev_id_number) == self.prev_Bricks[1].field_id): # If Bahn kommt von links
                        self.field_id = "".join(prev_id_letter+str(int(prevprev_id_number)+1))
                        self.directionFromPrevToCurrentBrick = "unten"
                    else: # If Bahn kommt von unten
                        self.field_id = "".join(chr(ord(prev_id_letter)-1)+prev_id_number)
                        self.directionFromPrevToCurrentBrick = "rechts"

                if(self.prev_Bricks[1].rotation >= -100 and self.prev_Bricks[1].rotation <= -80):
                    if("".join(prevprev_id_letter+str(int(prevprev_id_number)-1)) == self.prev_Bricks[1].field_id): # If Bahn kommt von unten
                        self.field_id = "".join(chr(ord(prev_id_letter)-1)+prev_id_number)
                        self.directionFromPrevToCurrentBrick = "links"
                    else: # if Bahn kommt von rechts
                        self.field_id = "".join(prev_id_letter+str(int(prev_id_number)+1))
                        self.directionFromPrevToCurrentBrick = "unten"
            return ""

    '''def getNextOrientation(self):
        if(nextBrick.type == 0): #straight
            if(self.directionFromPrevToCurrentBrick == "left" or self.directionFromPrevToCurrentBrick == "right"):
                self.next_Rotation = 90
            if(self.directionFromPrevToCurrentBrick == "oben" or self.directionFromPrevToCurrentBrick == "unten"):
                self.next_Rotation = 0

        else:
            if(self.directionFromPrevToCurrentBrick == "left"):
                pass
            if(self.directionFromPrevToCurrentBrick == "right"):
                pass'''

    def robotClient(self):
        print("Socket oeffnen")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.178.107', 5001))
            s.send(bytes(self.next_fieldID))
            s.close()
        except Exception as e:
            print("Error:",e)
            raise
