package PACKAGE_NAME;public class Z1 {
  public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        a:{ while (true)
        {
            b:{ String str = s.nextLine();
                String str1 = str.trim();
                int ch1 = 0;
                int ch2 = 0;
                int dl = str1.length();
                int a = str1.codePointAt(0);
                int b = str1.codePointAt(dl - 1);
                int c;
                int d;
                int e;
                int f;
                boolean r1 = false;
                boolean r2 = false;
                if (str1.equals("Стоп") | str1.equals("Stop")) {
                    break a;
                }
                if (dl < 3) {
                    try {
                        throw new Exception();
                    } catch (Exception ex) {
                        System.out.println("throws Exception //т.к. строка не является математической операцией");
                        break b;
                    }
                }
                if (!(48 <= a && a <= 57)) {
                    if (a == 73 || a == 86 || a == 88) {
                        r1 = true;
                    } else {
                        try {
                            throw new Exception();
                        } catch (Exception ex) {
                            System.out.println("throws Exception //т.к. строка не является математической операцией");
                            break b;
                        }
                    }
                }
                if (!(48 <= b && b <= 57)) {
                    if (b == 73 || b == 86 || b == 88) {
                        r2 = true;
                    } else {
                        try {
                            throw new Exception();
                        } catch (Exception ex) {
                            System.out.println("throws Exception //т.к. строка не является математической операцией");
                            break b;
                        }
                    }
                }
                if (!r1 && !r2) {
                    c = str1.codePointAt(1);
                    if (c==48 && a==49) {
                        ch1 = 10;
                    } else if (49 <= a) {
                        ch1 = a - 48;
                    }
                }
                if (!r1 && !r2) {
                    c = str1.codePointAt(dl-2);
                    if (b==48 && c==49) {
                        ch2 = 10;
                    } else if (49 <= b) {
                        ch2 = b - 48;
                    }
                }
                if (r1 && r2) {
                    char[] chars = str1.toCharArray();
                    if (chars[0] == 'I') {
                        if (chars[1] == 'I') {
                            if (chars[2] == 'I') {
                                ch1 = 3;
                            } else {
                                ch1 = 2;
                            }
                        } else if (chars[1] == 'V') {
                            ch1 = 4;
                        } else if (chars[1] == 'X') {
                            ch1 = 9;
                        } else {
                            ch1 = 1;
                        }
                    } else if (chars[0] == 'V') {
                        if (chars[1] == 'I') {
                            if (chars[2] == 'I') {
                                if (chars[3] == 'I') {
                                    ch1 = 8;
                                } else {
                                    ch1 = 7;
                                }
                            } else {
                                ch1 = 6;
                            }
                        } else {
                            ch1 = 5;
                        }
                    } else {
                        ch1 = 10;
                    }
                    if (chars[dl-1]=='X'){
                        if (chars[dl-2]=='I'){
                            ch2=9;
                        } else {
                            ch2=10;
                        }
                    } else if (chars[dl-1]=='V') {
                        if (chars[dl-2]=='I'){
                            ch2=4;
                        } else {
                            ch2=5;
                        }
                    } else {
                        if (chars[dl-2]=='V'){
                            ch2=6;
                        } else if (chars[dl-2]=='I') {
                            if (chars[dl-3]=='V'){
                                ch2=7;
                            } else if (chars[dl-3]=='I') {
                                if (chars[dl-4]=='V'){
                                    ch2=8;
                                } else {
                                    ch2=3;
                                }
                            } else {
                                ch2=2;
                            }
                        } else {
                            ch2=1;
                        }
                    }
                }
                c = str1.indexOf(43);
                int c1 = str1.indexOf(43,c+1);
                d = str1.indexOf(45);
                int d1 = str1.indexOf(45,d+1);
                e = str1.indexOf(42);
                int e1 = str1.indexOf(43,e+1);
                f = str1.indexOf(47);
                int f1 = str1.indexOf(47,f+1);
                int r;
                if ((c>=0 & (c1>=0 | d>=0 | e>=0 | f>=0)) | (d>=0 & (c>=0 | d1>=0 | e>=0 | f>=0)) | (e>=0 & (c>=0 | d>=0 | e1>=0 | f>=0)) | (f>=0 & (c>=0 | d>=0 | e>=0 | f1>=0))){
                    try {
                        throw new Exception();
                    } catch (Exception ex) {
                        System.out.println("throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)");
                        break b;
                    }
                }
                if (c >= 0) {
                    r = ch1 + ch2;
                } else if (d >= 0) {
                    r = ch1 - ch2;
                    if (r1 & r2 & r<=0){
                        try {
                            throw new Exception();
                        } catch (Exception ex) {
                            if (r==0){
                                System.out.println("throws Exception //т.к. в римской системе нет нуля");
                            } else {
                                System.out.println("throws Exception //т.к. в римской системе нет отрицательных чисел");
                            }
                            break b;
                        }
                    }
                } else if (e >= 0) {
                    r = ch1 * ch2;
                } else if (f >= 0) {
                    r = ch1 / ch2;
                    if (r1 & r2 & r==0){
                        try {
                            throw new Exception();
                        } catch (Exception ex) {
                            System.out.println("throws Exception //т.к. в римской системе нет нуля");
                            break b;
                        }
                    }
                } else {
                    try {
                        throw new Exception();
                    } catch (Exception ex) {
                        System.out.println("throws Exception //т.к. строка не является математической операцией");
                        break b;
                    }
                }
                outer:
                {   if (r1 && r2 && r>=1 && r<=100)
                {   if (r==100){
                    System.out.println("C");
                    break outer;
                } else if (r/90==1) {
                    r=r-90;
                    System.out.print("XC");
                } else if (r/50==1) {
                    r=r-50;
                    System.out.print("L");
                } else if (r/40==1) {
                    r=r-40;
                    System.out.print("XL");
                }
                    if (r/10>=1) {
                        int i=r/10;
                        r=r-(10*i);
                        while (i>=1){
                            i=i-1;
                            System.out.print("X");
                        }
                    }
                    if (r/9==1){
                        r=r-9;
                        System.out.print("IX");
                    } else if (r/5==1) {
                        r=r-5;
                        System.out.print("V");
                    } else if (r/4==1) {
                        r=r-4;
                        System.out.print("IV");
                    }
                    while (r>=1){
                        r=r-1;
                        System.out.print("I");
                    }
                } else if (!r1 && !r2 && r>=-100 && r<=100) {
                    System.out.print(r);
                } else if (!(r1==r2)) {
                    try {
                        throw new Exception();
                    } catch (Exception ex) {
                        System.out.println("throws Exception //т.к. используются одновременно разные системы счисления");
                        break b;
                    }
                } else {
                    try {
                        throw new Exception();
                    } catch (Exception ex) {
                        System.out.println("throws Exception //т.к. строка не является математической операцией");
                        break b;
                    }
                }
                    System.out.println();
                }
            }
        }
        }
        System.out.println("Программа закончила работу.");
    }
}
