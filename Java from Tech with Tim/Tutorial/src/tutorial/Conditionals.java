package tutorial;
import java.util.Scanner;

public class Conditionals {

	public static void main(String[] args) {
		System.out.print("Enter your age here: ");
		Scanner sc = new Scanner(System.in);
		String MyString = sc.next();
		int age = Integer.parseInt(MyString);
		
		if (age <= 13) {
			System.out.println("You cannot ride the rollercoaster!");
		}
		
		else {
			System.out.println("You may ride the rollercoaster");
		}
	}
		
		
	}
