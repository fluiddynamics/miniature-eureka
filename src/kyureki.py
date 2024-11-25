def css(writer):
    # writer.debug(5)
    writer.orientation("VVHHH")
    writer.font()
    writer.fit(0)
    writer.width(2, "6ch", True)
    writer.width(4, "11ch", False)
    writer.undisplay(2)

    writer.navy("d-29")

    writer.border_around(0)
    writer.border_mid(1,add=1)
    writer.border_mid(4)
    writer.border0(2,"left",add=">span")
    writer.border0(2, "right", add=">span")

    writer.padding("0.4ch")
    writer.sticky(2)
    writer.header()
