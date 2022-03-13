class Data2{
    int x;

    public void change(Data2 data){
        data.x=10000;
        System.out.println("===================");
        System.out.println(data.x);
    }
}

class test{
    public static void main(String[] args) {

        Data2 d = new Data2();
        d.x =10;
        System.out.println(d.x);

        d.change(d);
        System.out.println("******************");
        System.out.println(d.x);
    }

}