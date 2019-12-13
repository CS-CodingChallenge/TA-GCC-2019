import { print, image, promptString, promptNumber } from "introcs";
export let main = async () => {

    print("Welcome to the Federation Population Database!");
    print("(Post Book 2)");
    let bleh = await promptString("Would you like to learn information? (Yes/No)");

    while (bleh === "Yes") {
    let response: string = await promptString("What would you like to know about? (People/Governments/Events)");
    if (response === "People") {
        let answer = await promptNumber("Pick a place to learn about (Choose Number): 1-Brian Adams, " +
                                         "2-Emma Swift, 3-Jane, 4-Sayah Jefferson");
        if (answer === 1) {
            print("Brian Adams (male) Age 25");
            print("Born: March 11, 2108. Died: N/A. Height: 6 feet. Weight: 183 pounds. Eye color: Blue. Hair color: Brown.");
            print("Affiliations: Boston Mercs (2122-2126), RRA (2127-2133), FA (2108-2122, 2133).");
            print("Profession: Mercenary (2122-2133), Federation Special Operative-Infiltration Division (2133).");
            print("Current known associates: Emma Swift (girlfriend), Daniel Boran, Isabella Adams (sister).");
        } else {
            if (answer === 2) {
                print("Emma Swift (female) Age 24");
                print("Born: September 3, 2109. Died: N/A. Height: 5 feet 7 inches. Weight: 139 pounds. Eye color: Blue. Hair color: Blonde.");
                print("Affiliations: FA (2109-2133)");
                print("Profession: Inventor at American University (2130-2133), Federation Special Operative-Infiltration Divison (2133)");
                print("Current known associates: Brian Adams (boyfriend), Isabella Adams, Daniel Boran");
            } else {
                if (answer === 3) {
                    print("Jane (female) Age 43");
                    print("Born: 2090. Died: N/A. Height: 5 feet, 5 inches. Weight: 137 pounds. Eye color: Jade. Hair color: Black.");
                    print("Affiliations: WCS (2090-2119), RRA (2121-2133), Golden Order (2133-present)");
                    print("Profession: unknown (2092-2121), President of RRA (2121-2133), President of Golden Order (2133-present)");
                    print("Current known associates: Commander Lennox Washington");
                } else {
                    if (answer === 4) {
                        print("Sayah Jefferson (female) Age 23");
                        print("Born: 2110. Died: 2133. Height: 5 feet 9 inches. Weight: 153 pounds. Eye color: Green. Hair color: hazel.");
                        print("Affiliations: RRA (2116-2133), Golden Order (2133)");
                        print("Profession: Rebellion Assassin (2127-2133), Federation Special Operative-Infiltration Division (2133)");
                        print("Past known associates: Jane, Commander Washington, Brian Adams");
                    } else {
                        print("Person not found.");
                    }
                }
            }
        }

    } else {
        if (response === "Governments") {
            let answer2 = await promptNumber("Pick a government to learn about (Choose Number): 1-Federation, 2-WCS, 3-RRA, 4-GCE");
            if (answer2 === 1) {
                print("Federation of America");
                print("Established in 2083 after the splitting up of the United States of America. Split due to the Federation's support of artificial intelligence, and the Coalition's opposition to it.");
                print("Consistes of the states including and east of Lousisiana, Arkansas, Missouri, Iowa, and Minnesota. Capital located in New York City, New York.");
                print("Presidents include Javon Lewis (59th: 2077-2085), Howard Stew (60th: 2085-2093), Abram Adams (61st: 2093-2101), Terry Swift (62nd: 2101-2109), Addison Womolo (63rd: 2109-2117), Helen Wong (64th: 2117-2125), Carson Woon (65th: 2125-2129), Nicolas Womolo (66th: 2129-2133) Terrance Swift (66th: 2133)");
                print("The Federation, solely a military state, mass produced artificially intelligent soldiers, and was one of the final nations that stood against the Golden Order during the Golden Wars.");
                print("Notable members of FA: Brian Adams, Isabella Adams, Daniel Boran, Emma Swift, Terrance Swift, Matheis Oreal, David Erson.");
                print("The Federation fell in late December, 2133, to the Golden Order.");
            } else {
                if (answer2 === 2) {
                    print("Western Coalition of States");
                    print("Established in 2083, the Coalition suceeded from the United States of America due to their opposition to the recently perfected AI.");
                    print("Consists of all states to the West of Louisiana, Arkansas, Missouri, Iowa, and Minnesota. Capital located in San Francisco, California.");
                    print("Directors include Harry Trang (2080-2097), Jake Nottrab (2097-2119), and Ryan Nottrab (2119-2133)");
                    print("The Coalition is known for its culture of hate for androids and large amounts of propaganda. It was the first nation to fall to the Golden Order.");
                    print("Notable members of the WCS: Jane (former), Serge Mallot (The Surge).");
                    print("The Coalition fell in late November, 2133, to the Golden Order.");
                } else {
                    if (answer2 === 3) {
                        print("Rebellion for the Restoration of America");
                        print("Established in 2121, The RRA was founded by Jane, an idealist and former member of the Coalition. Its intent is to usurp both governments of the former US and establish a new government similar to that of the US during the Golden Age of America.");
                        print("Based in Texas, with hideouts in Alaska, Pennsylvania, and Asheville.");
                        print("President: Jane.");
                        print("The RRA is known for hiring assassins and mercenaries, relying on secrecy and blaming either the FA or the WCS. A military government, the RRA possesses a very large military and a lot influence.");
                        print("Notable members of the RRA: Jane, Sayah Jefferson, Commander Washington, Brian Adams (former).");
                        print("The RRA formed the Golden Alliance and transitioned into the Golden Order in December, 2133.");
                    } else {
                        if (answer2 === 4) {
                            print("Great Canadian Empire");
                            print("The GCE, formed out of Canada in 2031, was a major part of the United Human Race.");
                            print("Canada, no capital.");
                            print("Kings/Queens include Mercury (2031-2056), Venus (2056-2085), Mars (2085-2108), Jupiter (2108-2133)");
                            print("The GCE is known for its incredible advances in medicine and defense technology, including a national force field capable of withstanding a nuke.");
                            print("Notable members of the GCE: King Jupiter");
                            print("The GCE was forced to surrender to the Golden Order in late December, 2133, just before New Year's Eve.");
                        } else {
                            print("Answer not valid");
                        }
                    }
                }
            }
        } else {
            if (response === "Events") {
                let answer3 = await promptNumber("Pick an event to learn about (Select Number): 1-Golden Age of America, 2-Second American Civil War, 3-Christmas Assault, 4-Siege of the Capital");
                if (answer3 === 1) {
                    print("Golden Age of America");
                } else {
                    if (answer3 === 2) {
                        print("Second American Civil War");
                    } else {
                        if (answer3 === 3) {
                            print("Christmas Assault");
                        } else {
                            if (answer3 === 4) {
                                print("Siege of the Capital");
                            }
                        }
                    }
                }
            } else {
                print("Answer not valid");
            }
        }
    }    
    bleh = await promptString("Would you like to know more information? (Yes/No)");
    }
    print("Thank you for using the Federation Population database! Have a nice day!");
};
main();