function area(metros) {
    area = metros * metros;
    return area;
}
var num = prompt("Digite um valor em metros: ");
document.write(" A area de" + num + "é" + area(num));