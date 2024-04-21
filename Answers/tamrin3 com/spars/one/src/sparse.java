public class sparse {
    int spars[][];
    int n;
    int m;
    public sparse(int spars[][],int n,int m){
        this.spars=spars;
        this.n=n;
        this.m=m;
    }
    public void transpose(){
        int array[][]=new int[m][n] ;
        for(int i = 0; i <n ; i++){
            for(int j = 0; j <m; j++){
               array[j][i]=spars[i][j];
            }
        }
        for(int i=0;i<3;i++){
            for(int j=0;j<n-1;j++){
                System.out.print(array[i][j]);
            }
            System.out.println("");
        }
    }
    public void change(int a,int b,int c){
       int arr[][]=bsearch(spars,0,n-1,a,b,c);
       for(int i=0;i<n-1;i++){
           for(int j=0;j<3;j++){
               System.out.print(arr[i][j]);
           }
           System.out.println("");
       }
    }
    public int[][] bsearch(int[][] array, int low, int high, int n, int m , int k) {
        if (low <= high) {
            int mid=(low+high)/2;
            if(n<array[mid][0]){
               return bsearch(array,low,mid-1,n,m,k);
            }
            else if(n>array[mid][0]){
               return bsearch(array,mid+1,high,n,m,k);
            }

            else if(n==array[mid][0]){
                int z=mid;
                while(array[z][0]==n) {
                    if(array[z][1]==m){
                        array[z][2]=k;
                        /* جايگذاری در سطر و ستون مورد نظر پیدا شده*/
                    }
                    z++;
                }
            }
        }
return array;
}
}
