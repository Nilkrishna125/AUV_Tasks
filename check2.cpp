#include<iostream>
using namespace std;

void arrange(char s[100],int see,int n){

	    char c='z';

            int k;
            for(int i=see;i<n;i++){
		    if(int(s[i])<=int(c)){
			    c=s[i];
			    k=i; 							        }
	  }
	char fuck=s[see];
	s[see]=c;
	s[k]=fuck;
	if((n-see)>2){
	arrange(s,see+1 ,n);
	}
}
int main(){
	    string strs[]={"act","pots","tops","cat","stop","hat"};
	    string strso[]={"act","pots","tops","cat","stop","hat"};
	    int n=6;
	    for(int i=0;i<n;i++){
		string s=strs[i];
		int k=strs[i].length();
		char g[strs[i].length()];
                for(int j=0;j<strs[i].length();j++){
		g[j]=s[j];		
		}						            
	        arrange(g,0,k);
	string h="";
for(int m=0;m<k;m++)h=h+g[m];
strs[i]=h;

	    }

string strs2[6];
	    for(int i=0;i<n;i++)strs2[i]=strs[i];
	    for(int i=0;i<n;i++){
		    for(int j=i+1;j<n;j++){
			    if(strs2[i]==strs2[j])strs2[i]=" ";
		    }
	    }
	    int sount=0;
	    for(int i=0;i<n;i++)if(strs2[i]==" ")sount++;
	    sount=6-sount;

	    string ii[sount];//storing diff. types  of strings
	    int j=0;
	    for(int i=0;i<n;i++){
		    if(strs2[i]!=" "){
			    ii[j]=strs2[i];
			    j++;
		    }
	    }
	    int jj[sount]={};
	    
	    for(int j=0;j<sount;j++){
		    for(int i=0;i<n;i++){
		    	if(ii[j]==strs[i])jj[j]++;
		    }
	    }

		   

	    for(int i=0;i<n;i++)cout<<strs[i]<<" ";cout<<endl;
	    cout<<"[";
	    
	    for(int i=0;i<sount;i++){
		    int moj=0;
		    cout<<"[";
	            for(int k=0;k<n;k++){
			    if(ii[i]==strs[k]){
				    moj++;
				    cout<<strso[k];
				    if(moj<jj[i])cout<<",";
			   }
		    }
		    cout<<"]";
		    if(i<sount-1)cout<<",";
	    }
	    cout<<"]";


	    
}
























