import pygame

from src.Character import Character


class Player1(Character):
    wall_collision = False
    current_sprite = None
    grounded = True
    gravity = 1
    jump_force = 25
    current_jump = jump_force

    jumping_left_animation_clock = 0
    jumping_right_animation_clock = 0

    def __init__(self, screen_x, screen_y, x, y, health, speed):
        super().__init__(screen_x, screen_y, x, y, health, speed)

    def update(self):

        # print("Player 1:", self.state, "Player 1:", self.grounded)

        if self.screen_y >= 520:
            self.screen_y = 520
            self.current_jump = self.jump_force
            self.grounded = True

        else:
            self.grounded = False

        # print("Player x:", self.x, "Player y:", self.y)
        # print("Player screen_x:", self.screen_x, "Player screen_y:", self.screen_y)

        if self.animation_tick == 10000:
            self.animation_tick = 0
        self.animation_tick += 1

        if self.state == "standing" and not self.grounded:
            self.y += self.current_jump
            self.current_jump -= self.gravity
            self.screen_y -= self.current_jump

        elif self.state == "walking left" and not self.grounded:
            if self.x <= 0:
                pass
            elif self.wall_collision:
                self.screen_x -= self.speed * 1.5
                self.x -= self.speed

            else:
                self.screen_x = 420
                self.x -= self.speed

            self.y += self.current_jump
            self.current_jump -= self.gravity
            self.screen_y -= self.current_jump

        elif self.state == "walking right" and not self.grounded:

                if self.x >= 1020:
                    pass
                elif self.wall_collision:
                    self.screen_x += self.speed * 1.5
                    self.x += self.speed
                else:
                    self.screen_x = 420
                    self.x += self.speed

                self.y += self.current_jump
                self.current_jump -= self.gravity
                self.screen_y -= self.current_jump

        elif self.state == "walking left" and self.grounded:
            if self.x <= 0:
                pass
            elif self.wall_collision:
                self.screen_x -= self.speed * 1.5
                self.x -= self.speed
            else:
                self.screen_x = 420
                self.screen_y = 520
                self.x -= self.speed
        elif self.state == "walking right" and self.grounded:

            if self.x >= 1020:
                pass
            elif self.wall_collision:
                self.screen_x += self.speed * 1.5
                self.x += self.speed
            else:
                self.screen_x = 420
                self.screen_y = 520
                self.x += self.speed

        elif self.state == "jumping left":
            if self.x <= 0:
                pass
            elif self.wall_collision:
                self.screen_x -= self.speed * 1.5
                self.x -= self.speed
            else:
                self.screen_x = 420
                self.x -= self.speed

            self.y += self.current_jump
            self.current_jump -= self.gravity
            self.screen_y -= self.current_jump

        elif self.state == "jumping right":

            if self.x >= 1020:
                pass
            elif self.wall_collision:
                self.screen_x += self.speed * 1.5
                self.x += self.speed
            else:
                self.screen_x = 420
                self.x += self.speed

            self.y += self.current_jump
            self.current_jump -= self.gravity
            self.screen_y -= self.current_jump
        elif self.state == "jumping up":
            if self.grounded:
                self.current_jump = self.jump_force
                self.y += self.current_jump
                self.current_jump -= self.gravity
                self.screen_y -= self.current_jump
            else:
                self.y += self.current_jump
                self.current_jump -= self.gravity
                self.screen_y -= self.current_jump

    def draw(self, window):

        standing_animation_clock = self.animation_tick % 60
        walking_left_animation_clock = self.animation_tick % 63
        walking_right_animation_clock = self.animation_tick % 72

        if self.grounded:
            self.jumping_left_animation_clock = 0
            self.jumping_right_animation_clock = 0

        else:
            self.jumping_left_animation_clock += 1
            self.jumping_right_animation_clock += 1

        if self.state == "standing" and self.grounded:
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
        elif self.state == "standing" and not self.grounded:
            if self.facing == "left":
                if self.jumping_left_animation_clock < 10:
                    window.blit(self.images["jumping_left"][0], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][0]
                elif self.jumping_left_animation_clock < 20:
                    window.blit(self.images["jumping_left"][1], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][1]
                elif self.jumping_left_animation_clock < 30:
                    window.blit(self.images["jumping_left"][2], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][2]
                elif self.jumping_left_animation_clock < 40:
                    window.blit(self.images["jumping_left"][3], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][3]
                elif self.jumping_left_animation_clock < 50:
                    window.blit(self.images["jumping_left"][4], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][4]
                elif self.jumping_left_animation_clock < 60:
                    window.blit(self.images["jumping_left"][5], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][5]
                else:
                    window.blit(self.images["jumping_left"][6], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][6]
            elif self.facing == "right":
                if self.jumping_right_animation_clock < 10:
                    window.blit(self.images["jumping_right"][0], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][0]
                elif self.jumping_right_animation_clock < 20:
                    window.blit(self.images["jumping_right"][1], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][1]
                elif self.jumping_right_animation_clock < 30:
                    window.blit(self.images["jumping_right"][2], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][2]
                elif self.jumping_right_animation_clock < 40:
                    window.blit(self.images["jumping_right"][3], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][3]
                elif self.jumping_right_animation_clock < 50:
                    window.blit(self.images["jumping_right"][4], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][4]
                elif self.jumping_right_animation_clock < 60:
                    window.blit(self.images["jumping_right"][5], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][5]
                else:
                    window.blit(self.images["jumping_right"][6], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][6]
        elif self.state == "walking left" and self.grounded:
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
        elif self.state == "walking right" and self.grounded:
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
        elif self.state == "jumping left":
            if self.jumping_left_animation_clock < 10:
                window.blit(self.images["jumping_left"][0], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][0]
            elif self.jumping_left_animation_clock < 20:
                window.blit(self.images["jumping_left"][1], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][1]
            elif self.jumping_left_animation_clock < 30:
                window.blit(self.images["jumping_left"][2], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][2]
            elif self.jumping_left_animation_clock < 40:
                window.blit(self.images["jumping_left"][3], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][3]
            elif self.jumping_left_animation_clock < 50:
                window.blit(self.images["jumping_left"][4], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][4]
            elif self.jumping_left_animation_clock < 60:
                window.blit(self.images["jumping_left"][5], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][5]
            else:
                window.blit(self.images["jumping_left"][6], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][6]
        elif self.state == "jumping right":
            if self.jumping_right_animation_clock < 10:
                window.blit(self.images["jumping_right"][0], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][0]
            elif self.jumping_right_animation_clock < 20:
                window.blit(self.images["jumping_right"][1], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][1]
            elif self.jumping_right_animation_clock < 30:
                window.blit(self.images["jumping_right"][2], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][2]
            elif self.jumping_right_animation_clock < 40:
                window.blit(self.images["jumping_right"][3], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][3]
            elif self.jumping_right_animation_clock < 50:
                window.blit(self.images["jumping_right"][4], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][4]
            elif self.jumping_right_animation_clock < 60:
                window.blit(self.images["jumping_right"][5], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][5]
            else:
                window.blit(self.images["jumping_right"][6], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][6]
        elif self.state == "walking left" and not self.grounded:
            if self.jumping_left_animation_clock < 10:
                window.blit(self.images["jumping_left"][0], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][0]
            elif self.jumping_left_animation_clock < 20:
                window.blit(self.images["jumping_left"][1], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][1]
            elif self.jumping_left_animation_clock < 30:
                window.blit(self.images["jumping_left"][2], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][2]
            elif self.jumping_left_animation_clock < 40:
                window.blit(self.images["jumping_left"][3], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][3]
            elif self.jumping_left_animation_clock < 50:
                window.blit(self.images["jumping_left"][4], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][4]
            elif self.jumping_left_animation_clock < 60:
                window.blit(self.images["jumping_left"][5], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][5]
            else:
                window.blit(self.images["jumping_left"][6], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_left"][6]
        elif self.state == "walking right" and not self.grounded:
            if self.jumping_right_animation_clock < 10:
                window.blit(self.images["jumping_right"][0], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][0]
            elif self.jumping_right_animation_clock < 20:
                window.blit(self.images["jumping_right"][1], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][1]
            elif self.jumping_right_animation_clock < 30:
                window.blit(self.images["jumping_right"][2], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][2]
            elif self.jumping_right_animation_clock < 40:
                window.blit(self.images["jumping_right"][3], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][3]
            elif self.jumping_right_animation_clock < 50:
                window.blit(self.images["jumping_right"][4], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][4]
            elif self.jumping_right_animation_clock < 60:
                window.blit(self.images["jumping_right"][5], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][5]
            else:
                window.blit(self.images["jumping_right"][6], (self.screen_x, self.screen_y))
                self.current_sprite = self.images["jumping_right"][6]
        elif self.state == "jumping up":
            if self.facing == "left":
                if self.jumping_left_animation_clock < 10:
                    window.blit(self.images["jumping_left"][0], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][0]
                elif self.jumping_left_animation_clock < 20:
                    window.blit(self.images["jumping_left"][1], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][1]
                elif self.jumping_left_animation_clock < 30:
                    window.blit(self.images["jumping_left"][2], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][2]
                elif self.jumping_left_animation_clock < 40:
                    window.blit(self.images["jumping_left"][3], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][3]
                elif self.jumping_left_animation_clock < 50:
                    window.blit(self.images["jumping_left"][4], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][4]
                elif self.jumping_left_animation_clock < 60:
                    window.blit(self.images["jumping_left"][5], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][5]
                else:
                    window.blit(self.images["jumping_left"][6], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_left"][6]
            elif self.facing == "right":
                if self.jumping_right_animation_clock < 10:
                    window.blit(self.images["jumping_right"][0], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][0]
                elif self.jumping_right_animation_clock < 20:
                    window.blit(self.images["jumping_right"][1], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][1]
                elif self.jumping_right_animation_clock < 30:
                    window.blit(self.images["jumping_right"][2], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][2]
                elif self.jumping_right_animation_clock < 40:
                    window.blit(self.images["jumping_right"][3], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][3]
                elif self.jumping_right_animation_clock < 50:
                    window.blit(self.images["jumping_right"][4], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][4]
                elif self.jumping_right_animation_clock < 60:
                    window.blit(self.images["jumping_right"][5], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][5]
                else:
                    window.blit(self.images["jumping_right"][6], (self.screen_x, self.screen_y))
                    self.current_sprite = self.images["jumping_right"][6]

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
            elif self.current_sprite == self.images["standing_left"][1]:
                self.hitbox = pygame.Rect(self.screen_x + 10, self.screen_y, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())
            elif self.current_sprite == self.images["standing_left"][3]:
                self.hitbox = pygame.Rect(self.screen_x - 5, self.screen_y, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())
            elif self.current_sprite == self.images["standing_right"][1]:
                self.hitbox = pygame.Rect(self.screen_x - 10, self.screen_y, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())
            elif self.current_sprite == self.images["standing_right"][3]:
                self.hitbox = pygame.Rect(self.screen_x - 20, self.screen_y, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())
            else:
                self.hitbox = pygame.Rect(self.screen_x, self.screen_y, self.current_sprite.get_width(),
                                          self.current_sprite.get_height())

            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
