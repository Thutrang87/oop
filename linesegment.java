class Point {
    private int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public Point(Point p) {
        this.x = p.x;
        this.y = p.y;
    }
    public int getX() { return x; }
    public int getY() { return y; }
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
class LineSegment {
    private Point d1;
    private Point d2;
    public LineSegment() {
        this.d1 = new Point(8, 5);
        this.d2 = new Point(1, 0);
    }
    public LineSegment(Point d1, Point d2) {
        this.d1 = d1;
        this.d2 = d2;
    }
    public LineSegment(int x1, int y1, int x2, int y2) {
        this.d1 = new Point(x1, y1);
        this.d2 = new Point(x2, y2);
    }
    public LineSegment(LineSegment s) {
        this.d1 = new Point(s.d1);
        this.d2 = new Point(s.d2);
    }
    @Override
    public String toString() {
        return "d1" + d1 + " - d2" + d2;
    }
}
class Main {
    public static void main(String[] args) {
        LineSegment ls1 = new LineSegment();
        System.out.println("ls1: " + ls1);
        LineSegment ls2 = new LineSegment(3, 4, 7, 9);
        System.out.println("ls2: " + ls2);
        Point p1 = new Point(2, 3);
        Point p2 = new Point(5, 6);
        LineSegment ls3 = new LineSegment(p1, p2);
        System.out.println("ls3: " + ls3);
        LineSegment ls4 = new LineSegment(ls2);
        System.out.println("ls4 (copy of ls2): " + ls4);
    }
}
