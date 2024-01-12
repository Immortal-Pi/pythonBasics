from PIL import Image
def gifcreation(list1):

    # images=[]
    #
    # for arg in list1[1:]:
    #     image=Image.open(arg)
    #     images.append(image)
    #
    # images[0].save(
    #     "luffyFinal.gif",save_all=True, append_images=[images[1],images[2],images[3]],duration=200, loop=0
    # )


    images=[]

    for arg in list1[1:]:
        image=Image.open(arg)
        images.append(image)

    images[0].save(
        "joyboyfinal.gif",save_all=True, append_images=[images[1],images[2],images[3],images[4],images[5],images[6]], duration=200, loop=0
    )

    images=[]

    # for arg in list1[1:]:
    #     image=Image.open(arg)
    #     images.append(image)
    #
    # images[0].save(
    #     "king.gif", save_all=True, append_images=[images[1],images[2],images[3]], duration=10, loop=0
    # )
    # return