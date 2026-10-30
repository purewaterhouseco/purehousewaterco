"""Service-area water data for Pure House Water Co.

Each county: slug, name, overview, list of quick facts, and cities.
Each city: (name, utility, source or "", water type, local note).
Water type is one of: "City water", "City water + private wells", "Mostly private wells".
Facts are general; always confirm with an in-home test and the utility's annual
Consumer Confidence Report (CCR).
"""

CITY, MIXED, WELL = "City water", "City water + private wells", "Mostly private wells"

NTMWD = "North Texas Municipal Water District (Lavon Lake system)"

COUNTIES = [
    {
        "slug": "tarrant-county-tx",
        "name": "Tarrant County",
        "overview": "Most homes in Tarrant County are on city water that traces back to the Tarrant Regional Water District reservoir system. It's safe and treated, but it's hard — scale on faucets, shower glass and inside water heaters is something we see in nearly every home we test here.",
        "facts": [("Main supply", "Tarrant Regional Water District reservoirs"), ("Typical water type", CITY),
                  ("Disinfection", "Treated municipal supply (chloramine is common in the region)"), ("What we usually see", "Hard water & scale, chemical taste")],
        "cities": [
            ("Fort Worth", "Fort Worth Water", "Tarrant Regional Water District reservoirs", CITY,
             "Hardness from calcium and magnesium is the top complaint — crusty aerators, spotty dishes and water heaters that wear out early."),
            ("Arlington", "Arlington Water Utilities", "", CITY,
             "A large city system with consistently hard water. Softening plus carbon filtration is the most common fit."),
            ("Euless", "City of Euless", "", CITY,
             "Mid-cities homes on treated city water — hardness and taste are the usual reasons people call."),
            ("North Richland Hills", "City of North Richland Hills", "", CITY,
             "Many established neighborhoods where years of scale have already built up in plumbing and appliances."),
            ("Mansfield", "City of Mansfield", "", CITY,
             "Fast-growing with lots of newer homes — a great time to protect new fixtures and appliances from scale."),
            ("Keller", "City of Keller", "", CITY,
             "Larger homes with more bathrooms, so properly sizing the softener matters."),
            ("Southlake", "City of Southlake", "", CITY,
             "Larger homes and high water use — capacity and flow rate are key when we size a system here."),
            ("Grapevine", "City of Grapevine", "Lake Grapevine, blended with purchased treated water", CITY,
             "Because the supply is blended, taste can change through the year — carbon filtration helps keep it consistent."),
            ("Bedford", "City of Bedford", "", CITY,
             "Mature neighborhoods on city water where scale and chemical taste are the common issues."),
            ("Hurst", "City of Hurst", "", CITY,
             "City water with noticeable hardness; many homeowners start with a drinking water upgrade."),
        ],
    },
    {
        "slug": "dallas-county-tx",
        "name": "Dallas County",
        "overview": "Dallas County is served by several city utilities, some drawing from Dallas's own reservoirs and others from the North Texas Municipal Water District. The common thread is hard water — and older plumbing tends to show scale damage the fastest.",
        "facts": [("Main supply", "Dallas Water Utilities and NTMWD, by city"), ("Typical water type", CITY),
                  ("Disinfection", "Treated municipal supply (chloramine is common in the region)"), ("What we usually see", "Hard water, scale in older plumbing, taste & odor")],
        "cities": [
            ("Dallas", "Dallas Water Utilities", "Multiple regional reservoirs", CITY,
             "The supply is a blend from several lakes, so taste and hardness can shift seasonally."),
            ("Garland", "City of Garland", NTMWD, CITY,
             "Taste and smell are often a bigger complaint than hardness here — carbon filtration makes a big difference."),
            ("Irving", "Irving Water Utilities", "", CITY,
             "City water with typical North Texas hardness."),
            ("Mesquite", "City of Mesquite", "", CITY,
             "Many established neighborhoods where we regularly see water heaters damaged by scale."),
            ("Grand Prairie", "Grand Prairie Water Utilities", "", CITY,
             "The city spans more than one county, so water can differ depending on which side of town you're on."),
            ("Richardson", "City of Richardson", NTMWD, CITY,
             "Supplied by NTMWD rather than Dallas — a different water profile than the city next door."),
            ("Carrollton", "City of Carrollton", "", CITY,
             "Carrollton stretches across three counties, which is why testing your own tap beats relying on a citywide number."),
            ("DeSoto", "City of DeSoto", "", CITY,
             "Hard water and scale build-up in water heaters are common findings."),
            ("Cedar Hill", "City of Cedar Hill", "", CITY,
             "City water with typical regional hardness."),
        ],
    },
    {
        "slug": "collin-county-tx",
        "name": "Collin County",
        "overview": "Most of Collin County drinks water from Lavon Lake through the North Texas Municipal Water District. Lots of homes here are newer construction that has never had any treatment — which means scale starts building on day one.",
        "facts": [("Main supply", NTMWD), ("Typical water type", CITY),
                  ("Disinfection", "Treated municipal supply (chloramine is common in the region)"), ("What we usually see", "Hard water, scale on new fixtures")],
        "cities": [
            ("Plano", "City of Plano", NTMWD, CITY, "Hard NTMWD water — softening and filtration are the most common setup."),
            ("Frisco", "City of Frisco", NTMWD, CITY, "Lots of newer homes running with no treatment at all — ideal time to protect new appliances."),
            ("Allen", "City of Allen", NTMWD, CITY, "Same NTMWD supply as its neighbors, with the same scale issues."),
            ("Wylie", "City of Wylie", NTMWD, CITY, "Right next to Lavon Lake, the main reservoir for the district."),
            ("McKinney", "City of McKinney", "", CITY, "A fast-growing city on treated city water."),
            ("Celina", "City of Celina", "", CITY, "Mostly brand-new construction, usually with no water treatment installed."),
        ],
    },
    {
        "slug": "denton-county-tx",
        "name": "Denton County",
        "overview": "Denton County is a mix: city water in town, and private wells as you head out to acreage. Those two water types need very different systems — which is why we always test before recommending anything.",
        "facts": [("Main supply", "City utilities; Lewisville Lake for several cities"), ("Typical water type", MIXED),
                  ("Disinfection", "Treated municipal supply in town; untreated on private wells"), ("What we usually see", "Hardness; iron & sulfur on wells")],
        "cities": [
            ("Denton", "Denton Water Utilities", "", MIXED, "City water in town, private wells further out."),
            ("Lewisville", "City of Lewisville", "Lewisville Lake", CITY, "Seasonal taste and odor changes are common with lake water."),
            ("Flower Mound", "Town of Flower Mound", "", CITY, "Larger homes on city water — sizing the system correctly is key."),
            ("The Colony", "City of The Colony", "", CITY, "City water with typical North Texas hardness."),
            ("Corinth", "City of Corinth", "", MIXED, "Well properties nearby often deal with sulfur smell and iron staining."),
            ("Little Elm", "City of Little Elm", "Upper Trinity supply, Lewisville Lake", CITY, "Lakeside community on treated surface water."),
            ("Prosper", "Town of Prosper", "", CITY, "Mostly newer homes on city water."),
        ],
    },
    {
        "slug": "rockwall-county-tx",
        "name": "Rockwall County",
        "overview": "Nearly all of Rockwall County is on North Texas Municipal Water District supply. Homeowners are often surprised by how quickly scale builds up, even in homes that are only a few years old.",
        "facts": [("Main supply", NTMWD), ("Typical water type", CITY),
                  ("Disinfection", "Treated municipal supply (chloramine is common in the region)"), ("What we usually see", "Fast scale build-up")],
        "cities": [
            ("Rockwall", "City of Rockwall", NTMWD, CITY, "Even though Lake Ray Hubbard is right next door, Rockwall's tap water comes through NTMWD."),
            ("Rowlett", "City of Rowlett", "", CITY, "Many homes of a similar age, with similar water heater scale issues."),
            ("Heath", "City of Heath", "", CITY, "Larger homes that usually call for a higher-capacity system."),
            ("Royse City", "City of Royse City", "", CITY, "Mostly new construction, typically with no treatment installed."),
            ("Fate", "City of Fate", "", CITY, "One of the fastest-growing towns in the area — lots of homes only a few years old."),
        ],
    },
    {
        "slug": "ellis-county-tx",
        "name": "Ellis County",
        "overview": "In Ellis County, towns like Waxahachie and Midlothian treat local surface water, while acreage outside city limits is often on private wells. Two homes a few minutes apart can have completely different water.",
        "facts": [("Main supply", "City-treated local lakes; Rockett SUD in parts of the county"), ("Typical water type", MIXED),
                  ("Disinfection", "Treated in town; untreated on private wells"), ("What we usually see", "Hardness, seasonal taste & odor")],
        "cities": [
            ("Waxahachie", "City of Waxahachie", "Two local lakes, treated by the city", CITY, "The city treats its own lake water."),
            ("Midlothian", "City of Midlothian", "", MIXED, "City water in town — but just a few minutes out, many homes are on wells."),
            ("Ennis", "City of Ennis", "A local reservoir", CITY, "Seasonal taste and odor swings tend to be more noticeable here."),
            ("Red Oak", "Rockett Special Utility District (much of the area)", "", CITY, "Much of Red Oak is served by Rockett SUD rather than the city."),
        ],
    },
    {
        "slug": "johnson-county-tx",
        "name": "Johnson County",
        "overview": "Johnson County has city water in its towns, but well water is common once you get outside them — and with wells come iron staining and sulfur (rotten-egg) smell. Testing matters more here than almost anywhere.",
        "facts": [("Main supply", "City utilities and Johnson County SUD"), ("Typical water type", MIXED),
                  ("Disinfection", "Treated in town; untreated on private wells"), ("What we usually see", "Iron & sulfur on wells, hardness")],
        "cities": [
            ("Burleson", "City of Burleson", "Treated water purchased from Fort Worth", CITY, "Very similar water to Fort Worth since that's where it comes from."),
            ("Cleburne", "City of Cleburne", "Lake Pat Cleburne", CITY, "City water from its own lake."),
            ("Joshua", "Johnson County Special Utility District", "", CITY, "A utility district rather than a city system, so quality can vary more."),
            ("Alvarado", "City of Alvarado", "", MIXED, "Lots of acreage properties on private wells — testing is a must."),
        ],
    },
    {
        "slug": "parker-county-tx",
        "name": "Parker County",
        "overview": "Parker County is well-water country — big lots and private wells, especially outside city limits. Well water here regularly tests harder than city water and can carry iron, so we size every system to the actual test results.",
        "facts": [("Main supply", "Private wells; city and SUD systems in town"), ("Typical water type", WELL),
                  ("Disinfection", "Untreated on private wells"), ("What we usually see", "Very hard water, iron")],
        "cities": [
            ("Weatherford", "City of Weatherford", "", MIXED, "The city treats its own water; outside city limits, homes are on wells."),
            ("Aledo", "City of Aledo / Parker County SUD", "", MIXED, "A mix of treated supply and private wells."),
            ("Willow Park", "City of Willow Park", "", MIXED, "Mixed supplies across larger lots — a citywide average won't tell you much."),
            ("Springtown", "City of Springtown", "Groundwater", MIXED, "Groundwater typically means harder water and more iron."),
        ],
    },
    {
        "slug": "kaufman-county-tx",
        "name": "Kaufman County",
        "overview": "Kaufman County is growing fast. New neighborhoods are on North Texas Municipal Water District supply, while older properties are often still on private wells — where iron and sulfur are the usual problems.",
        "facts": [("Main supply", NTMWD + " for newer areas"), ("Typical water type", MIXED),
                  ("Disinfection", "Treated in town; untreated on private wells"), ("What we usually see", "Hardness; iron & sulfur on wells")],
        "cities": [
            ("Forney", "City of Forney", NTMWD, CITY, "Same supply as Garland and Mesquite; mostly new construction."),
            ("Terrell", "City of Terrell", "", CITY, "Older homes in central Terrell, where scale has had years to build up."),
            ("Kaufman", "City of Kaufman", "", MIXED, "City water in town; wells outside it, often with iron and sulfur."),
            ("Crandall", "City of Crandall", "", CITY, "Fast-growing with mostly new construction."),
        ],
    },
    {
        "slug": "hunt-county-tx",
        "name": "Hunt County",
        "overview": "Much of Hunt County's city water comes from Lake Tawakoni, and many homes on surrounding acreage are on private wells. Because supplies vary so much, we recommend testing rather than guessing.",
        "facts": [("Main supply", "Lake Tawakoni"), ("Typical water type", MIXED),
                  ("Disinfection", "Treated in town; untreated on private wells"), ("What we usually see", "Hardness, well-water variability")],
        "cities": [
            ("Greenville", "City of Greenville", "Lake Tawakoni", MIXED, "City water from the lake; wells are common on acreage east of town."),
            ("Caddo Mills", "City of Caddo Mills", "", MIXED, "A mix of city supply and wells."),
            ("Quinlan", "City of Quinlan", "", MIXED, "Near Lake Tawakoni, with many homes further out on wells."),
        ],
    },
    {
        "slug": "wise-county-tx",
        "name": "Wise County",
        "overview": "Wise County relies heavily on groundwater, and many homes are on private wells. Groundwater here usually tests harder than the reservoir-fed cities to the east.",
        "facts": [("Main supply", "Groundwater; Walnut Creek SUD in southern Wise County"), ("Typical water type", WELL),
                  ("Disinfection", "Untreated on private wells"), ("What we usually see", "Very hard water")],
        "cities": [
            ("Decatur", "City of Decatur", "Groundwater", CITY, "Groundwater supply that tends to be harder than lake-fed cities."),
            ("Bridgeport", "City of Bridgeport", "Its own lake", CITY, "One of the few cities here on surface water rather than groundwater."),
            ("Boyd", "City of Boyd / Walnut Creek SUD", "", MIXED, "Walnut Creek SUD covers much of the area, with many private wells."),
            ("Rhome", "City of Rhome", "Groundwater", CITY, "Usually groundwater rather than treated lake water."),
        ],
    },
]


def slugify(name):
    return name.lower().replace(" ", "-").replace("/", "")


TOTAL_CITIES = sum(len(c["cities"]) for c in COUNTIES)
