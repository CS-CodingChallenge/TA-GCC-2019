import { print } from "introcs";
export let main = async () => {
    let r = replicate([3, 2, 1]);
    let s = reverse([1, 2, 3, 4]);
    print(r);
    print(s);
};

let replicate = ( a: number[] ): number[] => {
    let b: number[] = [];
    for (let i = 0; i < a.length; i++) {
        for (let c = 0; c < a[i]; c++) {
            b[b.length] = a[i];
        }
    }
return b;
}

let reverse = (a: number[]): number[] => {
    let b: number[] = [];
    let c = 1;
    for (let i = 0; i < a.length; i++) {
        b[i] = a[a.length - c];
        c++;
    }
    return b;
}
main();