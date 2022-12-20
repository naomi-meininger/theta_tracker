const person = {
        first_name: "",
        last_name: "",
        password: "",
        num_points: 0,
        dues: 500,
        fullName : function() {
                return this.first_name + " " + this.last_name;
        }

};


function run() {

        // assume array was made beforehand

        println("Welcome to Theta Tracker!")
        var first = prompt("What is your first name?");
        var last = prompt("What is your last name?");
        var pass = prompt("What is your password?");
        let person = members.find(person => first_name === first && person => last_name === last && person => password === pass);

        // assume valid for now

        println("Welcome" + first + "!");
        println("What would you like to do?");
        println("Check Points (type p): ");
        println("Edit Points (type e): ");
        println("Check Dues (type d): ");
        var input = prompt("Choice: ");


        if (input == 'p') {
               println("You have " + person => num_points + "points.");

        } else if (input == 'e') {
                if (first != "Maddy" && last != Simms) {
                        println("You do not have access to this page");
                        return;
                }

        } else if (input == 'd') {
                println("Current dues: " + person => dues);

        } else {
                printlin("Invalid input");
        }



}