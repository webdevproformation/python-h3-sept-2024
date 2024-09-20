<?php 


class A{
    private $age ;

    public function setAge($valeur){
        if(gettype($valeur) === "int" &&  $valeur > 0){
            $this->age = $valeur;
        }
    }

    public function getAge(){
        return $this->age ; 
    }

}