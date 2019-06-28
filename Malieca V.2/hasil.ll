; ModuleID = "D:\2K19\Teknik Kompilasi\Malieca V.2\src\codegen.py"
target triple = "x86_64-pc-win32"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = mul i8 2, 5
  %".3" = bitcast [5 x i8]* @"fstr" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8 %".2")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"