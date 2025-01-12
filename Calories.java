import java.util.Scanner;
 
public class CalorieCounterPro {
    public static void main(String[] args) {
        System.out.println("Welcome to Calorie Counter Pro!");
 
        // Declare var
        String food1, food2, food3;
        int calories1, calories2, calories3;
        int totalCalories = 0;
 
        // New Read from input from the console
        java.util.Scanner scanner = new java.util.Scanner(System.in);
 
        System.out.println("Enter the name of the first food item:");
        food1 = scanner.nextLine();
        System.out.println("Enter the calories for " + food1 + ":");
        calories1 = scanner.nextInt();
        scanner.nextLine(); //newline
 
        System.out.println("Enter the name of the second food item:");
        food2 = scanner.nextLine();
        System.out.println("Enter the calories for " + food2 + ":");
        calories2 = scanner.nextInt();
        scanner.nextLine(); // newline
 
        System.out.println("Enter the name of the third food item:");
        food3 = scanner.nextLine();
        System.out.println("Enter the calories for " + food3 + ":");
        calories3 = scanner.nextInt();
        scanner.nextLine(); // Consume 
 
        // Calculate the total 
        totalCalories = calories1 + calories2 + calories3;
 
        
        System.out.println("\nYour Calorie Intake:");
        System.out.println("1. " + food1 + " - " + calories1 + " calories");
        System.out.println("2. " + food2 + " - " + calories2 + " calories");
        System.out.println("3. " + food3 + " - " + calories3 + " calories");
 
        
        System.out.println("\nTotal Calorie Intake: " + totalCalories + " calories");
 
        System.out.println("Thank you for using Calorie Counter Pro!");
        
        scanner.close(); // finish the scanner
    }
}
