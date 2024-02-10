import java.util.Scanner;
public class jac {
    public static void hoandoi(int[] z,int a,int b){
        int k = z[a];
        z[a] = z[b];
        z[b]= k;
    }
    public static void main(String[] args){
        int[] s = new int[10];
        Scanner in = new Scanner(System.in);
        for(int i = 0;i<10;i++){
            s[i] = in.nextInt();
        }
        for(int i = 0;i<9;i++){
            for(int j = i+1;j<10;j++){
                if(s[i]>s[j]){
                    hoandoi(s,i,j);
                }
            }
        }
        for(int x : s){
            System.out.print(x+" ");
        }
    }
}
