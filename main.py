import pygame

from classes.Post import Post
from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from helpers import screen
from helpers import mouse_in_button
from buttons import like_button, comment_button, click_post_button
from helpers import read_comment_from_user
from classes.Comment import Comment


def add_image(img_path, x_pos, y_pos, width, height):
    # Add the image to the screen
    img = pygame.image.load(img_path)
    img = pygame.transform.scale(img, (width, height))
    screen.blit(img, (x_pos, y_pos))


def main():
    post = Post("images/zelda2.jpg", "zelda",
                "good game!!!!!!")
    post2 = Post("images/sm64.jpg", "Home", "mario")
    post3 = Post("images/ronaldo.jpg","not Home","football")
    post4 = Post("images/mario2.jpg","Home","lego")
    post5 = Post("images/lg.jpg","Home","my new legos")
    post_list = [post, post2,post3,post4,post5]
    current_index = 0
    current_post = post_list[current_index]
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    # TODO (CLASS): set up background image(load and define size)
    add_image('images/background.png', 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, pos):
                    current_post.add_like()
                if mouse_in_button(comment_button, pos):
                    new_comment = read_comment_from_user()
                    comment = Comment(new_comment)
                    current_post.add_comment(comment)
                if mouse_in_button(click_post_button,pos):
                    current_index +=1
                    if current_index == len(post_list):
                        current_index = 0
                    current_post = post_list[current_index]
                    current_post.reset_comments_display_index()



                print(pos)

        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        # TODO (CLASS): display the background image
        add_image('images/background.png', 0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

        # TODO: Write the comment test here

        # TODO: call the test post here
        current_post.display()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.

        clock.tick(60)
    pygame.quit()
    quit()


main()
