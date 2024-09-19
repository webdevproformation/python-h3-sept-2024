<?php 

class A{
    public $nom = "Alain";
    public $age = 30;


    public function setAge($valeur){
        $this->age = $valeur ; 
    }
}

$a = new A(); 

var_dump($a->age); 