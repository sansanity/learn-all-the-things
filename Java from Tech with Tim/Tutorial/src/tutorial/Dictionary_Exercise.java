package tutorial;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;

public class Dictionary_Exercise {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Task: Given a string, create a hashmap that has the character as a key and the number of times it occurs as a value
		
		String test_string = "this is a test";
		
		Map myMap = new HashMap();
		
		for (char x: test_string.toCharArray()) {
			if (myMap.containsKey(x)){
				int old = (int) myMap.get(x);
				myMap.put(x, old+1);
			}
			else {
				myMap.put(x, 1);
			}
			System.out.println(myMap);
		}
		
		
	}

}
