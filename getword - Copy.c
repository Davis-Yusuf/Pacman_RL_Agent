#include "getword.h"

int getword( char *w )    
{
  int tempChar;              //Temporary variable to store characters from input
  int count;             //To count the number of characters
  int length;
  int prevChar;
  int isDollar;

  while ( ( tempChar = getchar() ) != EOF)       //While loop to collect all the characters and check for EOF
  {  
      //isDollar = 0; 
      if (tempChar == '$' && length == 0){
          isDollar = 1; 
      }
    if (tempChar == EOF){
            *w = '\0';
            count = length;
            length = 0;
            isDollar = 0;
            return count; 
    }

    if (prevChar == '$' && (tempChar == ' ' || tempChar == '\t')){
             w--;
             *w = '\0';
             prevChar = tempChar;
             length = 0;
             isDollar = 0;
             return 0;
    }
      if ( length == 0 )              
      {
        if (tempChar == ' ' || tempChar == '\t'){
            prevChar = tempChar;
            continue;
        }
      }
      
      if ( length != 0 )
      {
        if (prevChar == '\\' && tempChar == '\n'){
            w--;
            length--;
            *w = '\0';
            tempChar = ' ';
        }
        if (tempChar == ' ' || tempChar == '\t'){
            if (isDollar == 1){
                *w = '\0';
                isDollar = 0;
                count = length;
                length = 0;
                prevChar = tempChar;
                return -(count);
            }
            *w = '\0';
            count = length;
            length = 0;
            prevChar = tempChar;
            isDollar = 0;
            return count; 
        }
        else if ( tempChar == '\n' )
        {
            if (isDollar == 1){
                *w = '\0';
                ungetc ('\n', stdin);
                isDollar = 0;
                count = length;
                length = 0;
                prevChar = tempChar;
                return -(count);
            }
            *w = '\0';
            ungetc ('\n', stdin);
            count = length;
            length = 0;
            isDollar = 0;
            prevChar = tempChar;
            return count; 
        }
      }

      if ( tempChar == '\n' )                     
      {
        *w = '\0';
        prevChar = tempChar;
        length = 0;
        isDollar = 0;
        return 0;
      }
      
      else
      {
        if (tempChar == prevChar){
            continue; 
        }
        if (tempChar == '$' && length == 0){
            prevChar = tempChar;
            if (prevChar == '$'){
                *w = tempChar;
                w++;
                length++; 
            }
            continue; 
        }
        *w = tempChar;
        w++;
        length++; 
      }
      //isDollar = 0; 
      prevChar = tempChar;
      
  }
  *w = '\0';
  return -255;
  
}