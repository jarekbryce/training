void setup()
{
  size (640, 480);
  background(225);
}

void mouseDragged()
{
  line(pmouseX,pmouseY,mouseX, mouseY);
}
