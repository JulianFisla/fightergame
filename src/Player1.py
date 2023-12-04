from src.Character import Character


class Player1(Character):

    def __init__(self, screen_x, screen_y, x, y, health, speed):
        super().__init__(screen_x, screen_y, x, y, health, speed)

    def update(self):
        if self.animation_tick == 10000:
            self.animation_tick = 0
        self.animation_tick += 1
        # print("Player 1:", self.animation_tick)

        if self.state == "standing":
            self.x += 0
        elif self.state == "walking left":
            if self.x < 500:
                pass
            elif self.screen_x > 100:
                self.screen_x -= self.speed * 1.5
            else:
                self.x -= self.speed
        elif self.state == "crouching":
            self.x += 0
        elif self.state == "walking right":
            if self.screen_x > 800:
                pass
            elif self.x > 1030:
                self.screen_x += self.speed * 1.5
            else:
                self.x += self.speed

    def draw(self, window):

        standing_animation_clock = self.animation_tick % 60
        walking_left_animation_clock = self.animation_tick % 63
        walking_right_animation_clock = self.animation_tick % 72

        if self.state == "standing":
            if self.facing == "left":
                if standing_animation_clock < 15:
                    window.blit(self.images["standing_left"][0], (self.screen_x, self.screen_y))
                elif standing_animation_clock < 30:
                    window.blit(self.images["standing_left"][1], (self.screen_x, self.screen_y))
                elif standing_animation_clock < 45:
                    window.blit(self.images["standing_left"][2], (self.screen_x, self.screen_y))
                else:
                    window.blit(self.images["standing_left"][3], (self.screen_x, self.screen_y))
            elif self.facing == "right":
                if standing_animation_clock < 15:
                    window.blit(self.images["standing_right"][0], (self.screen_x, self.screen_y))
                elif standing_animation_clock < 30:
                    window.blit(self.images["standing_right"][1], (self.screen_x, self.screen_y))
                elif standing_animation_clock < 45:
                    window.blit(self.images["standing_right"][2], (self.screen_x, self.screen_y))
                else:
                    window.blit(self.images["standing_right"][3], (self.screen_x, self.screen_y))
        elif self.state == "walking left":
            if walking_left_animation_clock < 9:
                window.blit(self.images["running_left"][0], (self.screen_x, self.screen_y))
            elif walking_left_animation_clock < 18:
                window.blit(self.images["running_left"][1], (self.screen_x, self.screen_y - 70))
            elif walking_left_animation_clock < 27:
                window.blit(self.images["running_left"][2], (self.screen_x, self.screen_y))
            elif walking_left_animation_clock < 36:
                window.blit(self.images["running_left"][3], (self.screen_x, self.screen_y - 70))
            elif walking_left_animation_clock < 45:
                window.blit(self.images["running_left"][4], (self.screen_x, self.screen_y))
            elif walking_left_animation_clock < 54:
                window.blit(self.images["running_left"][5], (self.screen_x, self.screen_y - 70))
            else:
                window.blit(self.images["running_left"][6], (self.screen_x, self.screen_y))
        elif self.state == "walking right":
            if walking_right_animation_clock < 9:
                window.blit(self.images["running_right"][0], (self.screen_x, self.screen_y))
            elif walking_right_animation_clock < 18:
                window.blit(self.images["running_right"][1], (self.screen_x, self.screen_y - 70))
            elif walking_right_animation_clock < 27:
                window.blit(self.images["running_right"][2], (self.screen_x, self.screen_y))
            elif walking_right_animation_clock < 36:
                window.blit(self.images["running_right"][3], (self.screen_x, self.screen_y - 70))
            elif walking_right_animation_clock < 45:
                window.blit(self.images["running_right"][4], (self.screen_x, self.screen_y))
            elif walking_right_animation_clock < 54:
                window.blit(self.images["running_right"][5], (self.screen_x, self.screen_y - 70))
            elif walking_right_animation_clock < 63:
                window.blit(self.images["running_right"][6], (self.screen_x, self.screen_y))
            else:
                window.blit(self.images["running_right"][7], (self.screen_x, self.screen_y - 70))

