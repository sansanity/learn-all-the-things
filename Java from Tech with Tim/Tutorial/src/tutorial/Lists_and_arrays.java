package tutorial;
import java.util.Scanner;

public class Lists_and_arrays {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		int[] myarray = {12, 5 , 6, 7};
//		for (int i = 0; i <	 myarray.length; i+=1) {
//				System.out.println(myarray[i]);
//		}
//		
//		int count = 0;
//		
//		for (int element:myarray) {
//			System.out.println(element + " " + count);
//			count += 1;
//					
//		}
//		
//	}
		Scanner sc = new Scanner(System.in);
		String[] names = new String[5];
		for (int i = 0; i < names.length; i++) {
				System.out.print("Enter your Input: ");
				String input = sc.nextLine();
				names[i] = input;
		}

		for (int i = 0; i < names.length; i++) {
				System.out.println(names[i]);
		}
		
		for (String n: names) {
			System.out.println(n);
		}
	}
}
