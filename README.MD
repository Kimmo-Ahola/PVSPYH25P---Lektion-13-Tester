# Lägg till denna css

Inuti style.css i bankappen:

variabler inuti :root:
--color-btn-danger: #dc3547;
--color-btn-danger-hover: #da3142;
--color-btn-danger-text: #fff;
--color-btn-danger-border: #382f2f00;

klasser att lägga till:
.btn-danger{
  background-color: var(--color-btn-danger);
  color: var(--color-btn-danger-text);
  border: 1px solid var(--color-btn-danger-border);
}

.btn-secondary:hover{
    background-color: var(--color-btn-danger-hover);
}