<template>
    <p><b>Lista wydarzeń</b></p>
    Masz ochotę na konkretne wydarzenie? Chcesz się czegoś nauczyć? Poznać nową planszówkę? Nawiązać nowe znajomości? Daj znać, na pewno coś wymyślimy!<br><br>
	<div class="overflow-x-auto overflow-y-hidden">
		<table id="coming" v-if="events.length" CELLSPACING="0" class="dense">
			<thead>
				<tr>
					<th class="cell-small">Nazwa</th>
					<th class="cell-small">Data</th>
					<th class="cell-small">Godzina</th>
					<th class="cell-small">Rodzaj</th>
					<th class="cell-small">Zapisani</th>
					<th></th>
					<th class="cell-small">Opis</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(event, index) in events" :key="index">
					<td class="cell-small" v-html="event.name" />
					<td class="cell-small" v-html="getDateStringShort(event.start)" />
					<td
						class="cell-small border-left"
						v-html="getTimeStringShort(event.start)"
					/>
					<router-link class="cell-small" id="link" :to="`/event/${event.type}`">
						<td class="cell-small border-left" v-html="event.type" />
					</router-link>
					<td class="cell-small border-left" v-html="signed(event)" />
					<td>
						<button
							:disabled="!signedUser() || event.private"
							@click="event_signin(event.event_id)"
						>
							{{ button_text(event) }}
						</button>
					</td>
					<td class="cell-small border-left" v-html="event.description" />
				</tr>
			</tbody>
		</table>

        <p><b>Minione wydarzenia</b></p>
		<table v-if="past_events.length" CELLSPACING="0" class="dense">
			<thead>
				<tr>
					<th class="cell-small">Nazwa</th>
					<th class="cell-small">Data</th>
					<th class="cell-small">Godzina</th>
					<th class="cell-small">Rodzaj</th>
					<th class="cell-small">Zapisani</th>
					<th></th>
					<th class="cell-small">Opis</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(event, index) in past_events" :key="index">
					<td class="cell-small" v-html="event.name" />
					<td class="cell-small" v-html="getDateStringShort(event.start)" />
					<td
						class="cell-small border-left"
						v-html="getTimeStringShort(event.start)"
					/>
					<router-link class="cell-small" id="link" :to="`/event/${event.type}`">
						<td class="cell-small border-left" v-html="event.type" />
					</router-link>
					<td class="cell-small border-left" v-html="signed(event)" />
					<td>
						<button
							:disabled="!signedUser() || event.private"
							@click="event_signin(event.event_id)"
						>
							{{ button_text(event) }}
						</button>
					</td>
					<td class="cell-small border-left" v-html="event.description" />
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import { getDateStringShort, getTimeStringShort } from "../utils/date";
import axios_service from "../axios_service.js";
import { signedUser } from "../utils/auth";

export default {
	name: "Events",
	data() {
		return {
			events: [],
			past_events: [],
		};
	},
	mounted() {
        this.fetch_data()
	},
	methods: {
		getDateStringShort,
		getTimeStringShort,
		signedUser,
        fetch_data() {
            axios_service.get_events().then(({ data }) => {
                this.events = data["fut"];
                this.past_events = data["past"];
            });
        },
		signed(event) {
			if (event.limit == null) {
				return event.users.length;
			}
			return `${event.users.length}/${event.limit}`;
		},
		event_signin(event_id) {
            var text =this.button_text(event_id) 
			if (text == "WYPISZ SIĘ") {
				axios_service.event_signoff(event_id).then(() => {
                    this.fetch_data()
                })
			} else if (text == "ZAPISZ SIĘ") {
				axios_service.event_signin(event_id).then(() => {
                    this.fetch_data()
                })
			}
		},
		button_text(event) {
            if (event.private) {
                return "WYDARZENIE PRYWATNE"
            }
			for (var index in this.events) {
				var e = this.events[index];
				if (e.event_id == event.event_id) {
					if (signedUser() && e.users.indexOf(signedUser().username) !== -1) {
						return "WYPISZ SIĘ";
					}
				}
			}
			return "ZAPISZ SIĘ";
		},
	},
};
</script>

<style>
th,
td {
	border-bottom: none;
	text-align: left;
    line-height: 20px;

	padding-left: 16px;
	padding-right: 16px;

}
td {
	padding-bottom: 8px;
	padding-top: 8px;
}
th {
	color: white;
	background-image: linear-gradient(to right, #1c481c, #2b5d2a, #1c481c);
}
tbody:before {
	line-height: 1em;
	content: "\200C";
	display: block;
}
line {
      border: 200px solid red;

}
#coming {
    margin-bottom: 5em;
}
</style>

