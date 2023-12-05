import pygame

from src.Character import Character


class Player1(Character):
    wall_collision = False
    current_sprite = None

    def __init__(self, screen_x, screen_y, x, y, health, speed):
        super().__init__(screen_x, screen_y, x, y, health, speed)

    def update(self):

        # print("Player x:", self.x, "Player y:", self.y)

        if self.animation_tick == 10000:
            self.animation_tick = 0
        self.animation_tick += 1

        if self.state == "standing":
            self.x += 0
        elif self.state == "walking left":
            if self.x <= 0:
                pass
            elif self.wall_collision:
                self.screen_x -= self.speed * 1.5
                self.x -= self.speed
            else:
                self.x -= self.speed
        elif self.state == "crouching":
            self.x += 0
        elif self.state == "walking right":

            if self.x >= 1020:
                pass
            elif self.wall_collision:
                self.screen_x += self.speed * 1.5
                self.x += self.speed
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
                    self.current_sprite = self.images["standing_left"][0]
                elif standing_animation_clock < 30:
                    window.blit(self.images["standing_left"][1], (self.screen_x + 10, self.screen_y))
                    self.current_sprite = self.images["standing_left"][1]
                elif standing_animation_clock < 45:
                    window.blit(self.images["standing_left"][2], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["standing_left"][2]
                else:
                    window.blit(self.images["standing_left"][3], (self.screen_x - 5, self.screen_y))
                    self.current_sprite = self.images["standing_left"][3]
            elif self.facing == "right":
                if standing_animation_clock < 15:
                    window.blit(self.images["standing_right"][0], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["standing_right"][0]
                elif standing_animation_clock < 30:
                    window.blit(self.images["standing_right"][1], (self.screen_x - 10, self.screen_y))
                    self.current_sprite = self.images["standing_right"][1]
                elif standing_animation_clock < 45:
                    window.blit(self.images["standing_right"][2], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["standing_right"][2]
                else:
                    window.blit(self.images["standing_right"][3], (self.screen_x - 20, self.screen_y))
                    self.current_sprite = self.images["standing_right"][3]
        elif self.state == "walking left":
            if walking_left_animation_clock < 9:
                window.blit(self.images["running_left"][0], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_left"][0]
            elif walking_left_animation_clock < 18:
                window.blit(self.images["running_left"][1], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_left"][1]
            elif walking_left_animation_clock < 27:
                window.blit(self.images["running_left"][2], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_left"][2]
            elif walking_left_animation_clock < 36:
                window.blit(self.images["running_left"][3], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_left"][3]
            elif walking_left_animation_clock < 45:
                window.blit(self.images["running_left"][4], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_left"][4]
            elif walking_left_animation_clock < 54:
                window.blit(self.images["running_left"][5], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_left"][5]
            else:
                window.blit(self.images["running_left"][6], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_left"][6]
        elif self.state == "walking right":
            if walking_right_animation_clock < 9:
                window.blit(self.images["running_right"][0], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_right"][0]
            elif walking_right_animation_clock < 18:
                window.blit(self.images["running_right"][1], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_right"][1]
            elif walking_right_animation_clock < 27:
                window.blit(self.images["running_right"][2], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_right"][2]
            elif walking_right_animation_clock < 36:
                window.blit(self.images["running_right"][3], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_right"][3]
            elif walking_right_animation_clock < 45:
                window.blit(self.images["running_right"][4], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_right"][4]
            elif walking_right_animation_clock < 54:
                window.blit(self.images["running_right"][5], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_right"][5]
            elif walking_right_animation_clock < 63:
                window.blit(self.images["running_right"][6], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["running_right"][6]
            else:
                window.blit(self.images["running_right"][7], (self.screen_x, self.screen_y - 70))
                self.current_sprite = self.images["running_right"][7]

    def draw_hitbox(self, window):
        if self.current_sprite is not None:
            # print("width:", self.current_sprite.get_width())
            # print("height:", self.current_sprite.get_height())

            # print("screen_x", self.screen_x, "screen_y", self.screen_y)

            if self.current_sprite in (
                    self.images["running_left"][1], self.images["running_left"][3], self.images["running_left"][5],
                    self.images["running_right"][1], self.images["running_right"][3], self.images["running_right"][5],
                    self.images["running_right"][7]):
                self.hitbox = pygame.Rect(self.screen_x, self.screen_y - 70, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())
            else:
                self.hitbox = pygame.Rect(self.screen_x, self.screen_y, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())

            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
