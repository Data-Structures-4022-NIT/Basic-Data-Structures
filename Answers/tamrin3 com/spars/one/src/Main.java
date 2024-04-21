import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        int n=5;
        int m=6;
        int counter=0;
        int array[][]={{0,0,0,0,9,0},{0,8,0,0,0,0},{4,0,0,2,0,0},{0,0,0,0,0,5},{0,0,2,0,0,0}};
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(array[i][j]!=0){
                    counter++;
                }
            }
        }
        int c=0;
   int spars[][]=new int[counter][3];

        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(array[i][j]!=0){
                    spars[c][0]=i;
                    spars[c][1]=j;
                    spars[c][2]=array[i][j];
                }
            }
            c++;
        }
for(int i=0;i<counter-1;i++){
    for(int j=0;j<3;j++){
        System.out.print(spars[i][j]);
    }
    System.out.println("");
}
System.out.println("transpose");
sparse test=new sparse(spars,counter,3);
test.transpose();
int k=1;
int z=1;
int v=2;
System.out.println("change:");
test.change(k,z,v);
    }

}
