class Ex{
    public static void main(String args[]) {
        try {
            m1(10, 0);
            System.out.print("a");
        } catch (Exception e) {
            System.out.print("b");
        } finally {
            System.out.print("c");
        }
        System.out.println("d");
    }
    public static int m1(int data1, int data2) {
        return m2(data1, data2);
    }
    public static int m2(int data1, int data2) throws Exception {
        int result = data1 / data2;
        return result;
    }
}