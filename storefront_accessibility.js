// create storefront objects as classes
class Door {
  constructor(num, type) {
    // single or double
    this.num = num;
    // manual, automatic, or revolving
    this.type = type;
  }
  getNum() {return this.num;}
  getType() {return this.type;}
  getAccessibility() {
    if(this.type == "automatic") {return 0;}
    else if(this.type == "revolving") {return 3;}
    // double door (manual)
    else if(this.num == 2) {return 0;}
    // single door (manual)
    else {return 2;}
  }
}

class Stairs {
  constructor(num) {
    this.num = num;
  }
  getNum() {return this.num;}
  getAccessibility() {
    if(this.num == 0) {return 0;}
    else if(this.num == 1) {return 1;}
    else if(this.num == 2) {return 2;}
    else {return 3;}
  }
}

class Ramp {
  // ada is a boolean (TRUE - ada-regulated; FALSE - not ada-regulated)
  constructor(ada) {
    this.ada = ada;
  }
  getType() {return this.ada;}
  getAccessibility() {
    if(this.ada) {return 0;}
    else {return 1;}
  }
}

// storefront objects
var single_manual_door = new Door(1, "manual");
var double_manual_door = new Door(2, "manual");
var single_automatic_door = new Door(1, "automatic");
var double_automatic_door = new Door(2, "automatic");
var revolving_door = new Door(1, "revolving");
var stairs1 = new Stairs(1);
var stairs2 = new Stairs(2);
var stairs3 = new Stairs(3);
// make more stairs if necessary 
var ramp_ada = new Ramp(true);
var ramp_nonada = new Ramp(false);

// each store has its own dictionary
// all the stores are stored in an array
var all_stores = [];
var user_list = [];
var user_regions = [];
var user_categories = [];

// calculates the overall accessibility of the storefront
// takes in an array of storefront objects
function calculate_accessibility(objects) {
  // check if there is a ramp present
  var rampExists = false;
  for(var i = 0; i < objects.length; i++) {
    if(objects[i] instanceof Ramp) {rampExists = true;}
  }
  var accessibility_level = 0;
  // condition if ramp is present (ignore any stairs during calculation)
  if(rampExists) {
    for(var i = 0; i < objects.length; i++) {
      if(objects[i] instanceof Ramp) {
        accessibility_level += 0.6*(objects[i].getAccessibility())
      }
      else if(objects[i] instanceof Door) {
        accessibility_level += 0.4*(objects[i].getAccessibility())
      }
    }
  }
  // condition if ramp is not present
  else {
    for(var i = 0; i < objects.length; i++) {
      if(objects[i] instanceof Stairs) {
        accessibility_level += 0.6*(objects[i].getAccessibility())
      }
      else {
        accessibility_level += 0.4*(objects[i].getAccessibility())
      }
    }
  }
  return accessibility_level;
}

function sort_stores() {
  sort_town();
  sort_category();
  user_list = sort_accessibility();
}


// returns an array of stores within the specified town
function sort_town() {
  for(var i = 0; i < user_regions.length; i++) {
    for(var j = 0; j < all_stores.length; j++) {
      // split address so that we can retrieve the town name
      var temp_town = all_stores[j].address.split(', ')[1];
      // if the store's town matches the input town, then add it to the user's list of possible stores
      if(temp_town == user_regions[i]) {
        user_list.push(allstores[j]);
      }
    }
  }
}

// returns an array of stores within the specified category
function sort_category() {
  for(var i = user_list.length - 1; i > -1; i--) {
    var match = false;
    for(var j = 0; j < user_categories.length; j++) {
      var temp_category = user_list[i].category;
      // if the store's category matches the input category, then add it to the sorted list
      if(temp_category == user_categories[j]) {
        match = true;
      }
    }
    if(!match) {user_list.splice(i, 1)}
  }
}

// returns an array of stores sorted by accessibility level
function sort_accessibility() {
  user_list.sort(function(a, b) {
    return a.accessibility_level - b.accessibility_level;});
}
