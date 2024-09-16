```php 

class A(){
    private $largeur = 10;
    private $hauteur = 20 ;

    public function calcul(){
        return $this->largeur * $this->hauteur ;
    }
}
$a = A();
echo $a->calcul();

A->calcul($a)

```